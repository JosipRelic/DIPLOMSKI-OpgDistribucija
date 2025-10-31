from fastapi import APIRouter, Depends, HTTPException, Query, Path, Response
from sqlalchemy.orm import Session
from sqlalchemy import func, or_, and_, distinct
from typing import List, Optional, Dict, Any
from database import SessionLocal
from models import Opg, Proizvod, KategorijaProizvoda, Korisnik, KorisnickiProfil, Usluga, KategorijaUsluge, Recenzija
import math
from schemas import KreiranjeRecenzije
from security import dohvati_id_trenutnog_korisnika

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
    bez_recenzija: Optional[bool] = Query(default=False, description="true = samo opgovi bez recenzija"),
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
        .filter(Opg.verificiran == True)
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

    if bez_recenzija:
        podaci_opgova = podaci_opgova.filter(
            or_(Opg.broj_recenzija == 0, Opg.prosjecna_ocjena.is_(None))
        )
    else:
        if ocjena_min is not None:
            podaci_opgova = podaci_opgova.filter(
                Opg.prosjecna_ocjena.is_not(None)
            )

            if ocjena_min in (1,2,3,4):
                podaci_opgova = podaci_opgova.filter(
                    and_(Opg.prosjecna_ocjena >= ocjena_min, Opg.prosjecna_ocjena < ocjena_min + 1)
                )
            elif ocjena_min >= 5:
                podaci_opgova = podaci_opgova.filter(Opg.prosjecna_ocjena >= 5)

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
    
    subq = podaci_opgova.subquery()

    ukupno = db.query(func.count(func.distinct(subq.c.id))).scalar()
    ukupno_stranica = math.ceil(ukupno / velicina_stranice) if velicina_stranice else 0

    opg_ids = (
        db.query(subq.c.id)
        .distinct()
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
        "ukupno": ukupno,
        "ukupno_stranica": ukupno_stranica
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
            Opg.id.label("opg_id"),
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
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
                slika_proizvoda=proizvod.slika_proizvoda, slug=proizvod.slug, opg_id=proizvod.opg_id, opg_slug = proizvod.opg_slug,
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

@router.get("/statistika", response_model=Dict[str,int])
def statistika(
    db: Session = Depends(get_db)
):
    broj_registriranih_opgova = db.query(func.count(Opg.id)).filter(Opg.verificiran == True).scalar()
    broj_usluga = db.query(func.count(Usluga.id)).scalar()
    broj_proizvoda = db.query(func.count(Proizvod.id)).scalar()

    return{
        "broj_registriranih_opgova": int(broj_registriranih_opgova or 0),
        "broj_usluga": int(broj_usluga or 0),
        "broj_proizvoda": int(broj_proizvoda or 0)
    }


@router.get("/opgovi/{slug}")
def detalji_opga(slug: str, db:Session = Depends(get_db)):
    opg = (
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
            KorisnickiProfil.slika_profila,
            Korisnik.ime,
            Korisnik.prezime,
            Korisnik.broj_telefona,
            Korisnik.email.label("email")
        )
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .join(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Opg.slug == slug)
    ).first()

    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    return {
        "id": opg.id,
        "naziv": opg.naziv,
        "opis": opg.opis,
        "slug": opg.slug,
        "slika_profila": opg.slika_profila,
        "prosjecna_ocjena": float(opg.prosjecna_ocjena) if opg.prosjecna_ocjena is not None else None,
        "broj_recenzija": opg.broj_recenzija or 0,
        "adresa": opg.adresa,
        "grad": opg.grad,
        "postanski_broj": opg.postanski_broj,
        "zupanija": opg.zupanija,
        "ime": opg.ime,
        "prezime": opg.prezime,
        "broj_telefona": opg.broj_telefona,
        "email": opg.email
    }

@router.get("/opgovi/{slug}/kategorije-proizvoda")
def opg_kategorije_proizvoda(slug: str, db: Session = Depends(get_db)):
    opg = db.query(Opg.id).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    kategorije = (
        db.query(
            KategorijaProizvoda.id,
            KategorijaProizvoda.naziv,
            KategorijaProizvoda.slug,
            func.count(Proizvod.id).label("broj")
        )
        .join(Proizvod, Proizvod.kategorija_id == KategorijaProizvoda.id)
        .filter(Proizvod.opg_id == opg.id)
        .group_by(KategorijaProizvoda.id, KategorijaProizvoda.naziv, KategorijaProizvoda.slug)
        .order_by(KategorijaProizvoda.naziv.asc())
        .all()
    )

    return [{"id": kategorija.id, "naziv": kategorija.naziv, "slug": kategorija.slug, "broj": kategorija.broj} for kategorija in kategorije]


@router.get("/opgovi/{slug}/kategorije-usluga")
def opg_kategorije_usluga(slug: str, db: Session = Depends(get_db)):
    opg = db.query(Opg.id).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    kategorije = (
        db.query(
            KategorijaUsluge.id,
            KategorijaUsluge.naziv,
            KategorijaUsluge.slug,
            func.count(Usluga.id).label("broj")
        )
        .join(Usluga, Usluga.kategorija_id == KategorijaUsluge.id)
        .filter(Usluga.opg_id == opg.id)
        .group_by(KategorijaUsluge.id, KategorijaUsluge.naziv, KategorijaUsluge.slug)
        .order_by(KategorijaUsluge.naziv.asc())
        .all()
    )

    return [{"id": kategorija.id, "naziv": kategorija.naziv, "slug": kategorija.slug, "broj": kategorija.broj} for kategorija in kategorije]

@router.get("/opgovi/{slug}/proizvodi")
def opg_proizvodi(slug: str, db: Session = Depends(get_db), stranica: int = 1, velicina: int = 12, kat_slug: str | None = None):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen.")
    
    proizvodi = db.query(
        Proizvod.id,
        Proizvod.naziv,
        Proizvod.opis,
        Proizvod.cijena,
        Proizvod.mjerna_jedinica,
        Proizvod.slika_proizvoda,
        Proizvod.slug,
        Proizvod.kategorija_id,
        KategorijaProizvoda.slug.label("kategorija_slug")
    ).join(KategorijaProizvoda, KategorijaProizvoda.id == Proizvod.kategorija_id).filter(Proizvod.opg_id == opg.id)

    if kat_slug:
        kat = db.query(KategorijaProizvoda).filter_by(slug = kat_slug).first()
        if kat:
            proizvodi = proizvodi.filter(Proizvod.kategorija_id == kat.id)
            
    ukupno_proizvoda = proizvodi.count()
    lista_proizvoda = (
        proizvodi.order_by(Proizvod.naziv.asc()).offset((stranica-1)*velicina).limit(velicina).all()
    )

    return {
        "ukupno_proizvoda": ukupno_proizvoda,
        "lista_proizvoda": [
            dict(
                id = proizvod.id,
                naziv = proizvod.naziv,
                opis = proizvod.opis,
                cijena = float(proizvod.cijena),
                mjerna_jedinica = proizvod.mjerna_jedinica,
                slika_proizvoda = proizvod.slika_proizvoda,
                slug = proizvod.slug,
                kategorija_slug = proizvod.kategorija_slug,
                opg_id=opg.id,
            ) for proizvod in lista_proizvoda
        ]
    }


@router.get("/opgovi/{slug}/usluge")
def opg_usluge(slug:str, db: Session = Depends(get_db), stranica: int = 1, velicina: int = 12, kat_slug: str | None = None):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    usluge = db.query(Usluga).filter(Usluga.opg_id == opg.id)
    
    if kat_slug:
        kat = db.query(KategorijaUsluge).filter_by(slug=kat_slug).first()
        if kat: usluge = usluge.filter(Usluga.kategorija_id == kat.id)

    ukupno_usluga = usluge.count()
    lista_usluga = (usluge.order_by(Usluga.naziv.asc()).offset((stranica-1)*velicina).limit(velicina).all())

    return {
        "ukupno_usluga": ukupno_usluga,
        "lista_usluga": [
            dict(
                id = usluga.id,
                naziv = usluga.naziv,
                opis = usluga.opis,
                cijena = float(usluga.cijena),
                mjerna_jedinica = usluga.mjerna_jedinica,
                slika_usluge = usluga.slika_usluge,
                slug = usluga.slug,
                opg_naziv = usluga.opg.naziv
            ) for usluga in lista_usluga
        ]
    }


@router.get("/opgovi/{slug}/recenzije")
def opg_recenzije(
    slug: str,
    db: Session = Depends(get_db),
    stranica: int = 1,
    velicina: int = 10
):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    recenzije = (
        db.query(
            Recenzija.id,
            Recenzija.ocjena,
            Recenzija.komentar,
            Recenzija.datum_izrade,
            Korisnik.ime,
            Korisnik.prezime,
            KorisnickiProfil.slika_profila.label("slika_korisnika")
        )
        .outerjoin(Korisnik, Korisnik.id == Recenzija.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Recenzija.opg_id == opg.id)
        .order_by(Recenzija.datum_izrade.desc())
    )

    ukupno_recenzija = recenzije.count()
    rezultati = recenzije.offset((stranica - 1)*velicina).limit(velicina).all()

    return {
        "ukupno_recenzija": ukupno_recenzija,
        "recenzije": [
            dict(
                id = recenzija.id,
                ocjena = recenzija.ocjena,
                komentar = recenzija.komentar,              
                korisnik_ime = ("{} {}".format(recenzija.ime, recenzija.prezime).strip() if recenzija.ime or recenzija.prezime else None),
                datum_izrade = recenzija.datum_izrade.isoformat() if recenzija.datum_izrade else None,
                slika_korisnika = recenzija.slika_korisnika 
            ) for recenzija in rezultati
        ]
    }



@router.get("/opgovi/{slug}/moja-recenzija")
def moja_recenzija(
    slug: str,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika)
):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    recenzija = (
        db.query(
            Recenzija.id,
            Recenzija.ocjena,
            Recenzija.komentar,
            Recenzija.datum_izrade,
            Recenzija.datum_zadnje_izmjene
        )
        .filter(Recenzija.opg_id == opg.id, Recenzija.korisnik_id == id_trenutnog_korisnika)
        .first()
    )

    if not recenzija:
        return None
    
    return {
        "id": recenzija.id,
        "ocjena": recenzija.ocjena,
        "komentar": recenzija.komentar,
        "datum_izrade": recenzija.datum_izrade.isoformat() if recenzija.datum_izrade else None,
        "datum_zadnje_izmjene": recenzija.datum_zadnje_izmjene.isoformat() if recenzija.datum_zadnje_izmjene else None
    }


@router.put("/opgovi/{slug}/moja-recenzija")
def posalji_moju_recenziju(
    slug: str,
    body: KreiranjeRecenzije,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika)
):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    recenzija = (
        db.query(Recenzija)
        .filter(Recenzija.opg_id == opg.id, Recenzija.korisnik_id == id_trenutnog_korisnika)
        .first()
    )

    if recenzija is None:
        recenzija = Recenzija(
            opg_id = opg.id,
            korisnik_id = id_trenutnog_korisnika,
            ocjena = body.ocjena,
            komentar = (body.komentar or "").lstrip() or None
        )
        db.add(recenzija)
    else:
        recenzija.ocjena = body.ocjena
        recenzija.komentar = (body.komentar or "").lstrip() or None
        recenzija.datum_zadnje_izmjene = func.now()
    
    db.flush()

    izracun_prosjeka = (
        db.query(func.avg(Recenzija.ocjena), func.count(Recenzija.id))
        .filter(Recenzija.opg_id == opg.id)
        .first()
    )

    opg.prosjecna_ocjena = float(izracun_prosjeka[0]) if izracun_prosjeka[0] is not None else None
    opg.broj_recenzija = int(izracun_prosjeka[1] or 0)

    db.commit()
    db.refresh(recenzija)

    return {
        "id": recenzija.id,
        "ocjena": recenzija.ocjena,
        "komentar": recenzija.komentar,
        "datum_izrade": recenzija.datum_izrade.isoformat() if recenzija.datum_izrade else None,
        "datum_zadnje_izmjene": recenzija.datum_zadnje_izmjene.isoformat() if recenzija.datum_zadnje_izmjene else None,
        "prosjecna_ocjena": opg.prosjecna_ocjena,
        "broj_recenzija": opg.broj_recenzija
    }


@router.delete("/opgovi/{slug}/moja-recenzija", status_code=204)
def obrisi_moju_recenziju(
    slug: str,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika)
):
    opg = db.query(Opg).filter(Opg.slug == slug).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    
    recenzija = (
        db.query(Recenzija)
        .filter(Recenzija.opg_id == opg.id, Recenzija.korisnik_id == id_trenutnog_korisnika)
        .first()
    )

    if not recenzija:
        return Response(status_code=204)
    
    db.delete(recenzija)
    db.flush()

    izracun_prosjeka = (
        db.query(func.avg(Recenzija.ocjena), func.count(Recenzija.id))
        .filter(Recenzija.opg_id == opg.id)
        .first()
    )

    opg.prosjecna_ocjena = float(izracun_prosjeka[0]) if izracun_prosjeka[0] is not None else None
    opg.broj_recenzija = int(izracun_prosjeka[1] or 0)

    db.commit()
    return Response(status_code=204)