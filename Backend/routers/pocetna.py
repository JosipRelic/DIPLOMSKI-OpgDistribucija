from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal
from models import Proizvod, KategorijaProizvoda, Opg, Korisnik, KorisnickiProfil, NarudzbaStavka, Usluga


router = APIRouter(prefix="/pocetna", tags=["Početna"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def pocetna_istaknuto(db: Session = Depends(get_db)):
    najprodavaniji = (
        db.query(
            Proizvod.id.label("pid"),
            Proizvod.naziv,
            Proizvod.opis,
            Proizvod.cijena,
            Proizvod.slika_proizvoda,
            Proizvod.mjerna_jedinica,
            Proizvod.slug.label("proizvod_slug"),
            KategorijaProizvoda.slug.label("kategorija_slug"),
            Opg.id.label("opg_id"),
            Opg.slug.label("opg_slug"),
            Opg.naziv.label("opg_naziv"),
            func.sum(NarudzbaStavka.kolicina).label("uk_kolicina"),
        )
        .join(NarudzbaStavka, NarudzbaStavka.proizvod_id == Proizvod.id)
        .join(KategorijaProizvoda, KategorijaProizvoda.id == Proizvod.kategorija_id)
        .join(Opg, Opg.id == Proizvod.opg_id)
        .filter(
            NarudzbaStavka.tip == "proizvod",
            NarudzbaStavka.status != "otkazano",
            NarudzbaStavka.proizvod_id.isnot(None),
        )
        .group_by(
            Proizvod.id, Proizvod.naziv, Proizvod.opis, Proizvod.cijena,
            Proizvod.slika_proizvoda, Proizvod.mjerna_jedinica, Proizvod.slug,
            KategorijaProizvoda.slug, Opg.id, Opg.slug, Opg.naziv
        )
        .order_by(desc("uk_kolicina"))
        .limit(4)
        .all()
    )

    najprodavaniji_proizvodi = [{
        "id": p.pid,
        "naziv": p.naziv,
        "opis": p.opis,
        "cijena": float(p.cijena or 0),
        "slika_proizvoda": p.slika_proizvoda,
        "mjerna_jedinica": p.mjerna_jedinica,
        "slug": p.proizvod_slug,
        "kategorija_slug": p.kategorija_slug,
        "opg_id": p.opg_id,
        "opg_slug": p.opg_slug,
        "opg_naziv": p.opg_naziv,
    } for p in najprodavaniji]


    najbolje_ocijenjeni = (
        db.query(
            Opg.slug,
            Opg.naziv,
            Opg.prosjecna_ocjena,
            Opg.broj_recenzija,
            KorisnickiProfil.slika_profila,
            KorisnickiProfil.adresa,
            KorisnickiProfil.postanski_broj,
            KorisnickiProfil.grad,
        )
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Opg.verificiran == True)
        .order_by(
            Opg.prosjecna_ocjena.desc().nulls_last(),
            Opg.broj_recenzija.desc(),
            Opg.datum_pridruzivanja.desc(),
        )
        .limit(4)
        .all()
    )

    najbolje_ocijenjeni_opgovi = [{
        "slug": o.slug,
        "naziv": o.naziv,
        "prosjecna_ocjena": float(o.prosjecna_ocjena) if o.prosjecna_ocjena is not None else None,
        "broj_recenzija": int(o.broj_recenzija or 0),
        "slika_profila": o.slika_profila,
        "adresa": o.adresa,
        "postanski_broj": o.postanski_broj,
        "grad": o.grad,
    } for o in najbolje_ocijenjeni]


    najtrazenije = (
        db.query(
        Usluga.id,
        Usluga.naziv,
        Usluga.opis,
        Usluga.cijena,
        Usluga.mjerna_jedinica,
        Usluga.slika_usluge,
        Usluga.slug.label("usluga_slug"),
        Opg.id.label("opg_id"),
        Opg.slug.label("opg_slug"),
        Opg.naziv.label("opg_naziv"),
        func.sum(NarudzbaStavka.kolicina).label("zbroj"),
        )
        .join(NarudzbaStavka, NarudzbaStavka.usluga_id == Usluga.id)
        .join(Opg, Opg.id == Usluga.opg_id)
        .filter(NarudzbaStavka.status != "otkazano")
        .group_by(
            Usluga.id, Usluga.naziv, Usluga.opis, Usluga.cijena, Usluga.mjerna_jedinica,
            Usluga.slika_usluge, Usluga.slug, Opg.id, Opg.slug, Opg.naziv
        )
        .order_by(func.sum(NarudzbaStavka.kolicina).desc())
        .limit(4)
        .all()
    )

    najtrazenije_usluge = [{
        "usluga": {
            "id": u.id,
            "naziv": u.naziv,
            "opis": u.opis,
            "cijena": float(u.cijena or 0),
            "mjerna_jedinica": u.mjerna_jedinica,
            "slika_usluge": u.slika_usluge,
            "slug": u.usluga_slug,
            "opg_id": u.opg_id,
            "opg_slug": u.opg_slug,
            "opg_naziv": u.opg_naziv,
        },
        "usluga_slug_id": f"{u.usluga_slug}-{u.id}",
    } for u in najtrazenije]

    return {
        "najprodavaniji_proizvodi": najprodavaniji_proizvodi,
        "najbolje_ocijenjeni_opgovi": najbolje_ocijenjeni_opgovi,
        "najtrazenije_usluge": najtrazenije_usluge,
    }