from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from security import SessionLocal, dohvati_id_trenutnog_korisnika
from datetime import datetime, date
import time
from uuid import uuid4
from models import Narudzba, NarudzbaStavka, KosaricaStavka, Opg, OpgRaspolozivostPoDatumu, Proizvod, Usluga
from schemas import NarudzbaKreiranje, NarudzbaPrikaz
from mail import posalji_email_narudzbe_narucitelju, posalji_email_narudzbe_opg_primatelju

from routers.opg_raspolozivost import _oduzmi_rezervaciju_od_raspolozivosti


router = APIRouter(prefix="/narudzbe", tags=["Narudžbe"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=NarudzbaPrikaz)
def kreiraj_narudzbu(
    payload: NarudzbaKreiranje,
    db: Session = Depends(get_db),
    korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika),
):
    
    ts_ms = int(time.time() * 1000) 
    broj_narudzbe = f"{ts_ms}-{uuid4().hex[:6]}"
    
    iznos_bez_pdva = sum([(s.cijena / 1.25) * s.kolicina for s in payload.stavke])
    pdv = iznos_bez_pdva * 0.25


    narudzba = Narudzba(
        broj_narudzbe = broj_narudzbe,
        korisnik_id = korisnik_id,
        ime = payload.ime,
        prezime = payload.prezime,
        email = payload.email,
        telefon = payload.telefon,
        adresa = payload.adresa,
        grad = payload.grad,
        postanski_broj = payload.postanski_broj,
        zupanija = payload.zupanija,
        drzava = payload.drzava,
        nacin_placanja = payload.nacin_placanja,
        nacin_dostave = payload.nacin_dostave,
        iznos_bez_pdva = iznos_bez_pdva,
        pdv = pdv,
        dostava = None,
        ukupno = None,
    )

    opg_idevi = set()

    for s in payload.stavke:
        opg_id_stavka = None
        proizvod_id = None
        usluga_id = None
        termin_od_dt = None
        termin_do_dt = None

        if s.tip == "usluga" and s.termin_od and s.termin_do:
            try:
                termin_od_dt = datetime.fromisoformat(str(s.termin_od))
                termin_do_dt = datetime.fromisoformat(str(s.termin_do))
            except Exception:
                raise HTTPException(status_code=400, detail="Neispravan format termina za uslugu")
            if termin_do_dt <= termin_od_dt:
                raise HTTPException(status_code=400, detail="Završetak termina mora biti nakon početka")
    
        if s.tip == "usluga":
            if not s.usluga_id:
                raise HTTPException(status_code=400, detail="Nedostaje usluga_id")
            u = db.query(Usluga).get(s.usluga_id)
            if not u:
                raise HTTPException(status_code=400, detail="Usluga ne postoji")
            opg_id_stavka = u.opg_id
            usluga_id = s.usluga_id

        elif s.tip == "proizvod":
            if not s.proizvod_id:
                raise HTTPException(status_code=400, detail="Nedostaje proizvod_id")
            p = db.query(Proizvod).get(s.proizvod_id)
            if not p:
                raise HTTPException(status_code=400, detail="Proizvod ne postoji")
            opg_id_stavka = p.opg_id
            proizvod_id = s.proizvod_id

        if not opg_id_stavka:
            raise HTTPException(status_code=400, detail="Nije moguće odrediti OPG za stavku")

        opg_idevi.add(opg_id_stavka)

        stavka = NarudzbaStavka(
            tip=s.tip,
            proizvod_id = proizvod_id,
            usluga_id=s.usluga_id,
            naziv=s.naziv,
            kolicina=s.kolicina,
            mjerna_jedinica=s.mjerna_jedinica,
            cijena=s.cijena,
            slika=s.slika,
            termin_od=termin_od_dt,
            termin_do=termin_do_dt,
            opg_id = opg_id_stavka,
            status = "u_tijeku",
        )
        narudzba.stavke.append(stavka)

        dostava = 0
        if payload.nacin_dostave == "dostava":
            dostava = 5 * len(opg_idevi)

        narudzba.dostava = dostava
        narudzba.ukupno = iznos_bez_pdva + pdv + dostava
    
    db.add(narudzba)
    db.flush()

    for s in narudzba.stavke:
        if s.tip != "usluga" or not s.termin_od or not s.termin_do:
            continue

        try:
            dt_od = datetime.fromisoformat(str(s.termin_od))
            dt_do = datetime.fromisoformat(str(s.termin_do))
        except:
            raise HTTPException(status_code=400, detail="Neispravan format termina za uslugu")
        
        if dt_do <= dt_od:
            raise HTTPException(status_code=400, detail="Završetak termina mora biti nakon početka")
        
        usluga = db.query(Usluga).get(s.usluga_id) if hasattr(s, "usluga_id") else None
        if not usluga:
            raise HTTPException(status_code=400, detail="Nedostaje usluga za termin")
        
        opg_id = usluga.opg_id
        d = dt_od.date()
        if dt_do.date() != d:
            raise HTTPException(status_code=400, detail="Termin mora biti unutar jednog dana")
        
        pocetno_vrijeme = dt_od.hour * 60 + dt_od.minute
        zavrsno_vrijeme = dt_do.hour * 60 + dt_do.minute
        
        postoji_raspoloziv_termin = (
            db.query(OpgRaspolozivostPoDatumu)
            .filter(
                OpgRaspolozivostPoDatumu.opg_id == opg_id,
                OpgRaspolozivostPoDatumu.datum == d,
                OpgRaspolozivostPoDatumu.pocetno_vrijeme <= pocetno_vrijeme,
                OpgRaspolozivostPoDatumu.zavrsno_vrijeme >= zavrsno_vrijeme,
            ).first()
        )
        
        if not postoji_raspoloziv_termin:
            raise HTTPException(status_code=409, detail="Traženi termin više nije dostupan.")

        _oduzmi_rezervaciju_od_raspolozivosti(db, opg_id, d, pocetno_vrijeme, zavrsno_vrijeme)

    db.query(KosaricaStavka).filter(KosaricaStavka.korisnik_id == korisnik_id).delete(synchronize_session=False)

    db.commit()
    db.refresh(narudzba)

    try:
        posalji_email_narudzbe_narucitelju(narudzba.email, narudzba)
    except Exception as e:
        print("Greška pri slanju emaila kupcu:", e)

   
    try:
        opg_stavke = {}
        for s in narudzba.stavke:
            if not s.opg_id:
                continue
            if s.opg_id not in opg_stavke:
                opg_stavke[s.opg_id] = []
            opg_stavke[s.opg_id].append(s)

        kupac = {
            "ime": narudzba.ime,
            "prezime": narudzba.prezime,
            "email": narudzba.email,
            "telefon": narudzba.telefon,
            "adresa": f"{narudzba.adresa}, {narudzba.grad} {narudzba.postanski_broj}",
            "zupanija": narudzba.zupanija,
            "drzava": narudzba.drzava,
        }

        for opg_id, stavke in opg_stavke.items():
            opg = db.query(Opg).get(opg_id)
            if opg and opg.korisnik and opg.korisnik.email:
                posalji_email_narudzbe_opg_primatelju(opg.korisnik.email, opg.naziv, stavke, narudzba.broj_narudzbe, kupac, narudzba)
    except Exception as e:
        print("Greška pri slanju emaila OPG-ovima:", e)

    return narudzba
