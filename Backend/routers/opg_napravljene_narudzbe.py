import math
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal
from models import Korisnik, Opg, Narudzba, NarudzbaStavka
from security import dohvati_id_trenutnog_korisnika

router = APIRouter(prefix="/opg/napravljene-narudzbe", tags=["OPG profil - Napravljene narudžbe"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _moj_opg(db: Session, korisnik_id: int) -> Opg:
    k = db.get(Korisnik, korisnik_id)
    if not k or not k.opg:
        raise HTTPException(403, "Niste OPG korisnik")
    return k.opg


@router.get("")
def napravljene_narudzbe(
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    stranica: int = Query(1, ge=1),
    velicina: int = Query(8, ge=1, le=100),
    p: str | None = Query(None, description="pretraga po broju narudžbe"),
):
    moj_opg = _moj_opg(db, id_trenutnog_korisnika)

 
    narudzbe_lista = (
        db.query(Narudzba.id)
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(
            Narudzba.korisnik_id == id_trenutnog_korisnika,
            NarudzbaStavka.opg_id.isnot(None),
            NarudzbaStavka.opg_id != moj_opg.id,
        )
        .distinct()
    )

    if p:
        like = f"%{p.strip()}%"
        narudzbe_lista = narudzbe_lista.filter(Narudzba.broj_narudzbe.ilike(like))

   
    narudzbe_idevi_sq = narudzbe_lista.subquery()
    ukupno = db.query(func.count()).select_from(narudzbe_idevi_sq).scalar() or 0

    prikaz_narudzbi_po_stranici = (
        db.query(Narudzba.id)
        .filter(Narudzba.id.in_(db.query(narudzbe_idevi_sq.c.id)))
        .order_by(desc(Narudzba.datum_izrade))
        .offset((stranica - 1) * velicina)
        .limit(velicina)
        .all()
    )
    idevi = [i[0] for i in prikaz_narudzbi_po_stranici]

    if not idevi:
        return {"narudzbe": [], "ukupno": 0, "ukupno_stranica": 0}

    
    narudzbe = (
        db.query(Narudzba)
        .filter(Narudzba.id.in_(idevi))
        .order_by(desc(Narudzba.datum_izrade))
        .all()
    )

   
    rezultat = []
    for n in narudzbe:
 
        opgovi_lista = (
            db.query(Opg.naziv, Opg.slug)
            .join(NarudzbaStavka, NarudzbaStavka.opg_id == Opg.id)
            .filter(
                NarudzbaStavka.narudzba_id == n.id,
                NarudzbaStavka.opg_id.isnot(None),
                NarudzbaStavka.opg_id != moj_opg.id,
            )
            .distinct()
            .all()
        )
        opgovi = [{"naziv": o.naziv, "slug": o.slug} for o in opgovi_lista]

       
        s_set = {
            s[0]
            for s in db.query(NarudzbaStavka.status)
            .filter(
                NarudzbaStavka.narudzba_id == n.id,
                NarudzbaStavka.opg_id.isnot(None),
                NarudzbaStavka.opg_id != moj_opg.id,
            )
            .all()
        }
        if "otkazano" in s_set:
            status = "otkazano"
        elif s_set and s_set == {"isporuceno"}:
            status = "isporuceno"
        else:
            status = "u_tijeku"

        rezultat.append(
            {
                "narudzba_id": n.id,
                "broj_narudzbe": n.broj_narudzbe,
                "datum_izrade": n.datum_izrade.isoformat() if n.datum_izrade else None,
                "status": status,
              
                "iznos_bez_pdva": float(n.iznos_bez_pdva or 0.0),
                "pdv": float(n.pdv or 0.0),
                "dostava": float(n.dostava or 0.0),
                "ukupno": float(n.ukupno or 0.0),
                "opgovi": opgovi,  
            }
        )

    ukupno_stranica = math.ceil((ukupno or 0) / velicina)
    return {"narudzbe": rezultat, "ukupno": ukupno, "ukupno_stranica": ukupno_stranica}


@router.get("/detalji-narudzbe/{narudzba_id}")
def detalji_narudzbe(
    narudzba_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
):
    moj_opg = _moj_opg(db, id_trenutnog_korisnika)

    n = db.get(Narudzba, narudzba_id)
    if not n or n.korisnik_id != id_trenutnog_korisnika:
        raise HTTPException(404, "Narudžba nije pronađena")


    stavke = (
        db.query(
        NarudzbaStavka,
        Opg.naziv.label("opg_naziv"),
        Opg.slug.label("opg_slug"),
        )
        .join(Opg, Opg.id == NarudzbaStavka.opg_id)
        .filter(
            NarudzbaStavka.narudzba_id == narudzba_id,
            NarudzbaStavka.opg_id.isnot(None),
            NarudzbaStavka.opg_id != moj_opg.id,
        )
        .all()
    )

    if not stavke: 
        raise HTTPException(404, "Nema stavki od drugih OPG-ova u ovoj narudžbi.")

    
    proizvodi, usluge = [], []
    for s in stavke:
        opg_s = s[0]
        st = dict(
            id=opg_s.id,
            tip=opg_s.tip,
            naziv=opg_s.naziv,
            kolicina=opg_s.kolicina,
            mjerna_jedinica=opg_s.mjerna_jedinica,
            cijena=float(opg_s.cijena or 0),
            slika=opg_s.slika,
            termin_od=opg_s.termin_od.isoformat() if opg_s.termin_od else None,
            termin_do=opg_s.termin_do.isoformat() if opg_s.termin_do else None,
            status=opg_s.status,
            opg_naziv = s.opg_naziv,
            opg_slug = s.opg_slug,
        )
        (usluge if opg_s.tip == "usluga" else proizvodi).append(st)

   
    s_set = {s[0].status for s in stavke}
    if "otkazano" in s_set:
        status = "otkazano"
    elif s_set and s_set == {"isporuceno"}:
        status = "isporuceno"
    else:
        status = "u_tijeku"

   
    return {
       "id": n.id,
        "broj_narudzbe": n.broj_narudzbe,
        "datum_izrade": n.datum_izrade.isoformat() if n.datum_izrade else None,

    
        "iznos_bez_pdva": float(n.iznos_bez_pdva or 0.0),
        "pdv": float(n.pdv or 0.0),
        "dostava": float(n.dostava or 0.0),
        "ukupno": float(n.ukupno or 0.0),

        "status": status,
        "nacin_placanja": n.nacin_placanja,
        "nacin_dostave": n.nacin_dostave,

     
        "narucitelj": f"{(n.ime or '').strip()} {(n.prezime or '').strip()}".strip(),
        "kupac_email": n.email,
        "kupac_telefon": n.telefon,
        "adresa": f"{n.adresa}, {n.grad} {n.postanski_broj}".strip(", "),
        "zupanija": n.zupanija,

       
        "proizvodi": proizvodi,
        "usluge": usluge,
           
    }