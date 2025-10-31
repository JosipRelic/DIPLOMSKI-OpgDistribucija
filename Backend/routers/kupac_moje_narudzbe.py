import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import SessionLocal
from models import Korisnik, TipKorisnika, Narudzba, NarudzbaStavka, Opg
from security import dohvati_id_trenutnog_korisnika

router = APIRouter(prefix="/kupac/moje-narudzbe", tags=["Kupac profil - Moje narudžbe"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _kupac(db: Session, korisnik_id: int) -> Korisnik:
    k = db.get(Korisnik, korisnik_id)
    if not k or k.tip_korisnika != TipKorisnika.kupac:
        raise HTTPException(403, "Samo kupac može pristupiti svojim narudžbama")
    return k

def _status_narudzbe_iz_stavki(db: Session, narudzba_id: int) -> str:
    s_set = {
        s[0] for s in db.query(NarudzbaStavka.status)
        .filter(NarudzbaStavka.narudzba_id == narudzba_id).all()
    }
    if not s_set:
        return "u_tijeku"
    if "otkazano" in s_set:
        return "otkazano"
    if s_set == {"isporuceno"}:
        return "isporuceno"
    return "u_tijeku"

@router.get("")
def moje_narudzbe(
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    stranica: int = Query(1, ge=1),
    velicina: int = Query(10, ge=1, le=50),
    p: str | None = Query(None, description="pretraga po broju narudžbe")
):
    kupac = _kupac(db, id_trenutnog_korisnika)

    narudzbe = (
        db.query(
            Narudzba.id.label("nid"),
            Narudzba.broj_narudzbe,
            Narudzba.datum_izrade,
            Narudzba.nacin_dostave,
            Narudzba.ukupno,
        )
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(Narudzba.korisnik_id == kupac.id)
        .group_by(
            Narudzba.id,
            Narudzba.broj_narudzbe,
            Narudzba.datum_izrade,
            Narudzba.nacin_dostave,
            Narudzba.ukupno,
        )
    )

    if p:
        like = f"%{p.strip()}%"
        narudzbe = narudzbe.filter(Narudzba.broj_narudzbe.ilike(like))

    ukupno = narudzbe.count()

    prikaz_po_stranici = (
        narudzbe
        .order_by(desc(Narudzba.datum_izrade))
        .offset((stranica - 1) * velicina)
        .limit(velicina)
        .all()
    )

    stavke = []
    for st in prikaz_po_stranici:
        
        opg_nazivi_prikaz = (
            db.query(Opg.naziv, Opg.slug)
            .join(NarudzbaStavka, NarudzbaStavka.opg_id == Opg.id)
            .filter(NarudzbaStavka.narudzba_id == st.nid)
            .group_by(Opg.id, Opg.naziv, Opg.slug)  
            .all()
        )
        opgovi= [{"naziv": r[0], "slug": r[1]} for r in opg_nazivi_prikaz]

        status = _status_narudzbe_iz_stavki(db, st.nid)

        stavke.append({
            "narudzba_id": st.nid,
            "broj_narudzbe": st.broj_narudzbe,
            "datum_izrade": st.datum_izrade.isoformat() if st.datum_izrade else None,
            "status": status,
            "ukupno": round(st.ukupno, 2),
            "opgovi": opgovi,
        })

    return {
        "ukupno": ukupno,
        "stranica": stranica,
        "velicina": velicina,
        "stavke": stavke,
    }


@router.get("/detalji-narudzbe/{narudzba_id}")
def detalji_moje_narudzbe(
    narudzba_id: int,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
):
    kupac = _kupac(db, id_trenutnog_korisnika)

    n = db.query(Narudzba).filter(
        Narudzba.id == narudzba_id,
        Narudzba.korisnik_id == kupac.id
    ).first()

    if not n:
        raise HTTPException(404, "Narudžba nije pronađena.")

    proizvodi = (
        db.query(
            NarudzbaStavka.id,
            NarudzbaStavka.naziv,
            NarudzbaStavka.slika,
            NarudzbaStavka.kolicina,
            NarudzbaStavka.mjerna_jedinica,
            NarudzbaStavka.cijena,
            NarudzbaStavka.status,
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
        )
        .join(Opg, Opg.id == NarudzbaStavka.opg_id)
        .filter(
            NarudzbaStavka.narudzba_id == n.id,
            NarudzbaStavka.tip == "proizvod",
        )
        .all()
    )

    proizvodi_prikaz = [{
        "id": p.id,
        "naziv": p.naziv,
        "slika": p.slika,
        "kolicina": int(p.kolicina or 0),
        "mjerna_jedinica": p.mjerna_jedinica,
        "cijena": float(p.cijena or 0.0),
        "status": p.status,
        "opg_naziv": p.opg_naziv,
        "opg_slug": p.opg_slug,
    } for p in proizvodi]

    
    usluge = (
        db.query(
            NarudzbaStavka.id,
            NarudzbaStavka.naziv,
            NarudzbaStavka.slika,
            NarudzbaStavka.kolicina,
            NarudzbaStavka.mjerna_jedinica,
            NarudzbaStavka.cijena,
            NarudzbaStavka.status,
            NarudzbaStavka.termin_od,
            NarudzbaStavka.termin_do,
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
        )
        .join(Opg, Opg.id == NarudzbaStavka.opg_id)
        .filter(
            NarudzbaStavka.narudzba_id == n.id,
            NarudzbaStavka.tip == "usluga",
        )
        .all()
    )

    usluge_prikaz = [{
        "id": u.id,
        "naziv": u.naziv,
        "slika": u.slika,
        "kolicina": int(u.kolicina or 0),
        "mjerna_jedinica": u.mjerna_jedinica,
        "cijena": float(u.cijena or 0.0),
        "status": u.status,
        "termin_od": u.termin_od.isoformat() if u.termin_od else None,
        "termin_do": u.termin_do.isoformat() if u.termin_do else None,
        "opg_naziv": u.opg_naziv,
        "opg_slug": u.opg_slug,
    } for u in usluge]

    detalji = {
        "broj_narudzbe": n.broj_narudzbe,
        "proizvodi": proizvodi_prikaz,
        "usluge": usluge_prikaz,

        "iznos_bez_pdva": float(n.iznos_bez_pdva or 0.0),
        "pdv": float(n.pdv or 0.0),
        "dostava": float(n.dostava or 0.0),
        "ukupno": float(n.ukupno or 0.0),

        "narucitelj": f"{(n.ime or '').strip()} {(n.prezime or '').strip()}".strip(),
        "kupac_email": n.email,
        "kupac_telefon": n.telefon,
        "adresa": f"{n.adresa}, {n.grad} {n.postanski_broj}",
        "zupanija": n.zupanija,

        "nacin_placanja": n.nacin_placanja,
        "nacin_dostave": n.nacin_dostave,
    }

    return {"detalji": detalji}