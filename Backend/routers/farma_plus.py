import math
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, or_, case
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usluga, KategorijaUsluge, Opg, Korisnik, KorisnickiProfil

router = APIRouter(prefix="/farma-plus", tags=["Farma+"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/kategorije", response_model=List[Dict[str,Any]])
def kategorije_usluga(db: Session = Depends(get_db)):
    kategorije = (
        db.query(
            KategorijaUsluge.id,
            KategorijaUsluge.naziv,
            KategorijaUsluge.slug,
            func.count(Usluga.id).label("ukupno"),
            func.sum(case((Usluga.usluga_dostupna == True, 1), else_=0)).label("dostupni"),
            func.sum(case((Usluga.usluga_dostupna == False, 1), else_=0)).label("nedostupni")
        )
        .outerjoin(Usluga, Usluga.kategorija_id == KategorijaUsluge.id)
        .group_by(KategorijaUsluge.id, KategorijaUsluge.naziv, KategorijaUsluge.slug)
        .order_by(KategorijaUsluge.naziv.asc())
        .all()
    )

    return [
        {
            "id": kategorija.id,
            "naziv": kategorija.naziv,
            "slug": kategorija.slug,
            "ukupno": int(kategorija.ukupno or 0),
            "dostupni": int(kategorija.dostupni or 0),
            "nedostupni": int(kategorija.nedostupni or 0)
        } for kategorija in kategorije
    ]

@router.get("/filteri-lokacije", response_model=Dict[str, List[str]])
def filteri_lokacije(
    kat_slug: str = Query(..., description="Slug kategorije"),
    db: Session = Depends(get_db)
):
    kategorija = db.query(KategorijaUsluge).filter(KategorijaUsluge.slug == kat_slug).first()
    if not kategorija:
        raise HTTPException(status_code=404, detail="Kategorija ne postoji")
    
    podaci = (
        db.query(
            KorisnickiProfil.zupanija,
            KorisnickiProfil.grad,
            Usluga.naziv.label("usluga_naziv")
        )
        .join(Korisnik, Korisnik.id == KorisnickiProfil.korisnik_id)
        .join(Opg, Opg.korisnik_id == Korisnik.id)
        .join(Usluga, Usluga.opg_id == Opg.id)
        .filter(Usluga.kategorija_id == kategorija.id, Usluga.usluga_dostupna == True)
    ).all()

    zupanije_set, mjesta_set, usluge_set = set(), set(), set()
    for z, g, u in podaci:
        if z:
            zupanije_set.add(z.strip())
        if g:
            mjesta_set.add(g.strip())
        if u:
            usluge_set.add(u.strip())

    return {
        "zupanije": sorted(zupanije_set),
        "mjesta": sorted(mjesta_set),
        "usluge": sorted(usluge_set)
    }


@router.get("/usluge", response_model=Dict[str, Any])
def usluge(
    kat_slug: str = Query(...),
    q: Optional[str] = Query(None, description="pretraga po nazivu usluge ili OPG-a"),
    zupanije: List[str] = Query(default=[]),
    mjesta: List[str] = Query(default=[]),
    usluge: List[str] = Query(default=[]),
    sortiranje: str = Query("novo"),
    stranica: int = Query(1, ge=1),
    velicina_stranice: int = Query(12, ge=1, le=100),
    db: Session = Depends(get_db)
):
    kat = db.query(KategorijaUsluge).filter(KategorijaUsluge.slug == kat_slug).first()
    if not kat:
        raise HTTPException(status_code=404, detail="Kategorija ne postoji")
    
    dozvoljeno_sortiranje = {"novo", "naziv_asc", "naziv_desc", "cijena_asc", "cijena_desc"}
    if sortiranje not in dozvoljeno_sortiranje:
        raise HTTPException(status_code=400, detail="Nevažeća vrijednost za sortiranje")
    
    usluge_upit = (
        db.query(
            Usluga.id,
            Usluga.naziv,
            Usluga.opis,
            Usluga.cijena,
            Usluga.mjerna_jedinica,
            Usluga.slika_usluge,
            Usluga.slug,
            Usluga.usluga_dostupna,
            Usluga.opg_id,
            Usluga.datum_izrade,
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
            KorisnickiProfil.grad.label("grad"),
            KorisnickiProfil.zupanija.label("zupanija"),
        )
        .join(Opg, Opg.id == Usluga.opg_id)
        .join(Korisnik, Opg.korisnik_id == Korisnik.id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Usluga.kategorija_id == kat.id, Usluga.usluga_dostupna == True)
    )

    if q:
        like = f"%{q.strip()}%"
        usluge_upit = usluge_upit.filter(or_(Usluga.naziv.ilike(like), Opg.naziv.ilike(like)))
    if zupanije:
        usluge_upit = usluge_upit.filter(KorisnickiProfil.zupanija.in_(zupanije))
    if mjesta:
        usluge_upit = usluge_upit.filter(KorisnickiProfil.grad.in_(mjesta))
    if usluge:
        usluge_upit = usluge_upit.filter(Usluga.naziv.in_(usluge))

    if sortiranje == "naziv_asc":
        usluge_upit = usluge_upit.order_by(Usluga.naziv.asc())
    elif sortiranje == "naziv_desc":
        usluge_upit = usluge_upit.order_by(Usluga.naziv.desc())
    elif sortiranje == "cijena_asc":
        usluge_upit = usluge_upit.order_by(Usluga.cijena.asc(), Usluga.id.desc())
    elif sortiranje == "cijena_desc":
        usluge_upit = usluge_upit.order_by(Usluga.cijena.desc(), Usluga.id.desc())
    else:
        usluge_upit = usluge_upit.order_by(Usluga.datum_izrade.desc())

    ukupno_usluga = usluge_upit.count()
    offset = (stranica - 1) * velicina_stranice
    lista_usluga = usluge_upit.offset(offset).limit(velicina_stranice).all()

    return {
        "usluge": [
            {
                "id": usluga.id,
                "naziv": usluga.naziv,
                "opis": usluga.opis,
                "cijena": float(usluga.cijena) if usluga.cijena is not None else None,
                "slika_usluge": usluga.slika_usluge,
                "usluga_dostupna": usluga.usluga_dostupna,
                "mjerna_jedinica": usluga.mjerna_jedinica,
                "slug": usluga.slug,
                "opg_id": usluga.opg_id,
                "opg_naziv": usluga.opg_naziv,
                "opg_slug": usluga.opg_slug,
                "grad": usluga.grad,
                "zupanija": usluga.zupanija,
                "datum_izrade": usluga.datum_izrade
            } for usluga in lista_usluga
        ],
        "ukupno_usluga": ukupno_usluga,
        "ukupno_stranica": math.ceil(ukupno_usluga / velicina_stranice) if velicina_stranice else 1
    }