from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from security import SessionLocal, dohvati_id_trenutnog_korisnika
from datetime import datetime, date
import time
from uuid import uuid4
from models import Narudzba, NarudzbaStavka, KosaricaStavka, OpgRaspolozivostPoDatumu, Usluga
from schemas import NarudzbaKreiranje, NarudzbaPrikaz

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
    dostava = 5 if payload.nacin_dostave == "dostava" else 0
    ukupno = iznos_bez_pdva + pdv + dostava

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
        dostava = dostava,
        ukupno = ukupno,
    )

    for s in payload.stavke:
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
    
        stavka = NarudzbaStavka(
            tip=s.tip,
            usluga_id=s.usluga_id,
            naziv=s.naziv,
            kolicina=s.kolicina,
            mjerna_jedinica=s.mjerna_jedinica,
            cijena=s.cijena,
            slika=s.slika,
            termin_od=termin_od_dt,
            termin_do=termin_do_dt,
        )
        narudzba.stavke.append(stavka)
    
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

    return narudzba
