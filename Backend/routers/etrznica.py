from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from sqlalchemy import func, or_, and_, distinct
from typing import List, Optional, Dict, Any
from database import SessionLocal
from models import Opg, Proizvod, KategorijaProizvoda, Korisnik, KorisnickiProfil

router = APIRouter(prefix="/e-trznica", tags=["E-tržnica"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/kategorije", response_model=List[Dict[str, Any]])
def sve_kategorije_proizvoda(db: Session = Depends(get_db)):
    kategorije = (
        db.query(
            KategorijaProizvoda.id,
            KategorijaProizvoda.naziv,
            KategorijaProizvoda.slug,
            KategorijaProizvoda.opis,
            KategorijaProizvoda.slika_kategorije,
            func.count(Proizvod.id).label("broj_proizvoda")
        )
        .outerjoin(
            Proizvod, 
            Proizvod.kategorija_id == KategorijaProizvoda.id)
        .group_by(
            KategorijaProizvoda.id, 
            KategorijaProizvoda.naziv, 
            KategorijaProizvoda.slug, 
            KategorijaProizvoda.opis, 
            KategorijaProizvoda.slika_kategorije)
        .order_by(KategorijaProizvoda.naziv.asc())
        .all()
    )
    return [
        dict(
            id = kategorija.id,
            naziv = kategorija.naziv,
            slug = kategorija.slug,
            opis = kategorija.opis,
            slika_kategorije = kategorija.slika_kategorije,
            broj_proizvoda = int(kategorija.broj_proizvoda or 0)

        ) for kategorija in kategorije
    ]


@router.get("/kategorije/{slug}", response_model=Dict[str, Any])
def pojedina_kategorija_proizvoda(slug:str, db: Session = Depends(get_db)):
    kategorija = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == slug).first()
    if not kategorija:
        raise HTTPException(status_code=404, detail="Kategorija nije pronađena")
    return dict(
        id = kategorija.id,
        naziv = kategorija.naziv,
        slug = kategorija.slug,
        opis = kategorija.opis,
        slika_kategorije = kategorija.slika_kategorije
    )


@router.get("/filteri-lokacije", response_model=Dict[str, List[str]])
def filteri_lokacije(
    kat_slug: Optional[str] = Query(default=None, 
                                    description="Ako je zadana kategorija, vrati samo OPG-ove koji imaju proizvode iz te kategorije"),
    db: Session = Depends(get_db)
    ):

    q = (
        db.query(KorisnickiProfil.zupanija, KorisnickiProfil.grad)
        .join(Korisnik, Korisnik.id == KorisnickiProfil.korisnik_id)
        .join(Opg, Opg.korisnik_id == Korisnik.id)
    )

    if kat_slug:
        kategorija = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == kat_slug).first()
        if kategorija:
            q = q.join(Proizvod, Proizvod.opg_id == Opg.id).filter(Proizvod.kategorija_id == kategorija.id)
    
    zup_set, mj_set = set(), set()
    for z, g in q:
        if z: zup_set.add(z)
        if g: mj_set.add(g)
    
    return {"zupanije": sorted(zup_set), "mjesta": sorted(mj_set)}


@router.get("/opgovi", response_model=Dict[str, Any])
def opgovi(
    db: Session = Depends(get_db),
    q: Optional[str] = Query(default=None),
    zupanije: Optional[str] = Query(default=None, description="odvojeno-zarezom"),
    mjesta: Optional[str] = Query(default=None, description="odvojeno-zarezom"),
    ocjena_min: Optional[float] = Query(default=None),
    sortiranje: Optional[str] = Query(default=None, description="naziv_asc|naziv_desc|ocjena_desc|ocjena_asc") ,
    stranica: int = 1,
    velicina_stranice: int = 9,
    kat_slug: Optional[str] = Query(default=None, description="filtriraj OPG-ove koji imaju proizvode iz ove kategorije")
):
    
    podaci_opgova = (
        db.query(
            Opg.id,
            Opg.naziv,
            Opg.opis,
            Opg.slug,
            Opg.prosjecna_ocjena,
            Opg.broj_recenzija,
            KorisnickiProfil.adresa,
            KorisnickiProfil.grad,
            KorisnickiProfil.postanski_broj,
            KorisnickiProfil.zupanija,
            KorisnickiProfil.slika_profila
        )
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .join(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
    )

    if kat_slug:
        kategorija = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == kat_slug).first()
        if kategorija:
            podaci_opgova = podaci_opgova.join(Proizvod, Proizvod.opg_id == Opg.id).filter(Proizvod.kategorija_id == kategorija.id)
    
    if q:
        like = f"%{q.lower()}%"
        podaci_opgova = podaci_opgova.filter(or_(func.lower(Opg.naziv).like(like), func.lower(Opg.opis).like(like))) 
    
    if zupanije:
        podaci_opgova = podaci_opgova.filter(KorisnickiProfil.zupanija.in_(zupanije.split(",")))
    
    if mjesta:
        podaci_opgova = podaci_opgova.filter(KorisnickiProfil.grad.in_(mjesta.split(",")))

    if ocjena_min is not None:
        podaci_opgova = podaci_opgova.filter((Opg.prosjecna_ocjena != None) & (Opg.prosjecna_ocjena >= ocjena_min))
    

    if sortiranje == "naziv_asc":
        podaci_opgova = podaci_opgova.order_by(Opg.naziv.asc())
    elif sortiranje == "naziv_desc":
        podaci_opgova = podaci_opgova.order_by(Opg.naziv.desc())
    elif sortiranje == "ocjena_desc":
        podaci_opgova = podaci_opgova.order_by(Opg.prosjecna_ocjena.desc().nulls_last())
    elif sortiranje == "ocjena_asc":
        podaci_opgova = podaci_opgova.order_by(Opg.prosjecna_ocjena.asc().nulls_first())
    else:
        podaci_opgova = podaci_opgova.order_by(Opg.naziv.asc())
    

    ukupno = db.query(func.count(distinct(Opg.id))).select_from(podaci_opgova.subquery()).scalar()
    opg_ids = (
    db.query(distinct(Opg.id))
      .select_from(podaci_opgova.subquery())
      .offset((stranica - 1) * velicina_stranice)
      .limit(velicina_stranice)
      .all()
    )
    ids = [oid[0] for oid in opg_ids]
    prikaz_opgova = podaci_opgova.filter(Opg.id.in_(ids)).all()

    return {
        "opgovi": [
            dict(
                id = opg.id,
                naziv = opg.naziv,
                opis = opg.opis,
                slug = opg.slug,
                slika_profila = opg.slika_profila,
                prosjecna_ocjena = float(opg.prosjecna_ocjena) if opg.prosjecna_ocjena is not None else None,
                broj_recenzija = opg.broj_recenzija or 0,
                adresa = opg.adresa, 
                grad = opg.grad,
                postanski_broj = opg.postanski_broj,
                zupanija = opg.zupanija
            ) for opg in prikaz_opgova
        ],
        "ukupno": ukupno
    }


@router.get("/proizvodi", response_model=Dict[str, Any])
def proizvodi_po_kategoriji(
    db: Session = Depends(get_db),
    kat_slug: str = Query(..., description="slug kategorije"),
    q: Optional[str] = Query(default=None),
    zupanije: Optional[str] = Query(default=None, description="odvojeno-zarezom"),
    mjesta: Optional[str] = Query(default=None, description="odvojeno-zarezom"),
    sortiranje: Optional[str] = Query(default="novo", description="novo|naziv_asc|naziv_desc|cijena_asc|cijena_desc"),
    stranica: int = 1,
    velicina_stranice: int = 12,
):
    kat = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == kat_slug).first()
    if not kat:
        raise HTTPException(status_code=404, detail="Kategorija nije pronađena")

    ukupno_u_kategoriji = (
        db.query(func.count(Proizvod.id))
        .filter(Proizvod.kategorija_id == kat.id, Proizvod.proizvod_dostupan == True)
        .scalar()
    ) or 0

    podaci_proizvoda = (
        db.query(
            Proizvod.id, Proizvod.naziv, Proizvod.opis, Proizvod.cijena,
            Proizvod.mjerna_jedinica, Proizvod.slika_proizvoda, Proizvod.slug,
            Opg.naziv.label("opg_naziv"),
            KorisnickiProfil.grad, KorisnickiProfil.zupanija
        )
        .join(Opg, Opg.id == Proizvod.opg_id)
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .join(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Proizvod.kategorija_id == kat.id, Proizvod.proizvod_dostupan == True)
    )

    if q:
        like = f"%{q.lower()}%"
        podaci_proizvoda = podaci_proizvoda.filter(func.lower(Proizvod.naziv).like(like) | func.lower(Opg.naziv).like(like))

    if zupanije:
        podaci_proizvoda = podaci_proizvoda.filter(KorisnickiProfil.zupanija.in_(zupanije.split(",")))

    if mjesta:
        podaci_proizvoda = podaci_proizvoda.filter(KorisnickiProfil.grad.in_(mjesta.split(",")))

    if sortiranje == "naziv_asc":
        podaci_proizvoda = podaci_proizvoda.order_by(Proizvod.naziv.asc())
    elif sortiranje == "naziv_desc":
        podaci_proizvoda = podaci_proizvoda.order_by(Proizvod.naziv.desc())
    elif sortiranje == "cijena_asc":
        podaci_proizvoda = podaci_proizvoda.order_by(Proizvod.cijena.asc())
    elif sortiranje == "cijena_desc":
        podaci_proizvoda = podaci_proizvoda.order_by(Proizvod.cijena.desc())
    else:
        podaci_proizvoda = podaci_proizvoda.order_by(Proizvod.datum_izrade.desc())

    ukupno = podaci_proizvoda.count()
    proizvodi = podaci_proizvoda.offset((stranica - 1) * velicina_stranice).limit(velicina_stranice).all()

    return {
        "proizvodi": [
            dict(
                id=proizvod.id, naziv=proizvod.naziv, opis=proizvod.opis,
                cijena=float(proizvod.cijena), mjerna_jedinica=proizvod.mjerna_jedinica,
                slika_proizvoda=proizvod.slika_proizvoda, slug=proizvod.slug,
                opg_naziv=proizvod.opg_naziv, grad=proizvod.grad, zupanija=proizvod.zupanija
            ) for proizvod in proizvodi
        ],
        "ukupno": ukupno,
        "ukupno_u_kategoriji": ukupno_u_kategoriji
    }

@router.get("/proizvodi/{proizvod_id}", response_model=Dict[str, Any])
def detalji_proizvoda(
    proizvod_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
):
    proizvod = (
        db.query(
            Proizvod.id, 
            Proizvod.naziv, 
            Proizvod.opis, 
            Proizvod.cijena,
            Proizvod.mjerna_jedinica,
            Proizvod.slika_proizvoda,
            Proizvod.slug,
            Proizvod.proizvod_dostupan,
            Opg.id.label("opg_id"),
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
            KorisnickiProfil.grad,
            KorisnickiProfil.zupanija,
            KategorijaProizvoda.naziv.label("kategorija_naziv"),
            KategorijaProizvoda.slug.label("kategorija_slug")
        ) 
        .join(Opg, Opg.id == Proizvod.opg_id)
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .join(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .join(KategorijaProizvoda, KategorijaProizvoda.id == Proizvod.kategorija_id)
        .filter(Proizvod.id == proizvod_id)
        .first()
    )
    if not proizvod:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen")
    
    return {
        "id": proizvod.id,
        "naziv": proizvod.naziv,
        "opis": proizvod.opis,
        "cijena": float(proizvod.cijena),
        "mjerna_jedinica": proizvod.mjerna_jedinica,
        "slika_proizvoda": proizvod.slika_proizvoda,
        "slug": proizvod.slug,
        "proizvod_dostupan": proizvod.proizvod_dostupan,
        "opg": {
            "id": proizvod.opg_id,
            "naziv": proizvod.opg_naziv,
            "slug": proizvod.opg_slug,
            "grad": proizvod.grad,
            "zupanija": proizvod.zupanija
        },
        "kategorija": {
            "naziv": proizvod.kategorija_naziv,
            "slug": proizvod.kategorija_slug
        }
    }