from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal
from models import KategorijaProizvoda, KategorijaUsluge, KorisnickiProfil, Korisnik, Proizvod, TipKorisnika, Narudzba, NarudzbaStavka, Opg, Usluga
from security import dohvati_id_trenutnog_korisnika

router = APIRouter(prefix="/kupac/nadzorna-ploca", tags=["Kupac profil - Nadzorna ploča"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _kupac(db: Session, korisnik_id: int) -> Korisnik:
    k = db.get(Korisnik, korisnik_id)
    if not k or k.tip_korisnika != TipKorisnika.kupac:
        raise HTTPException(403, "Samo kupac može pristupiti nadzornoj ploči kupca")
    return k

@router.get("")
def kupac_nadzorna_ploca(
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
):
    kupac = _kupac(db, id_trenutnog_korisnika)

   
    ukupno_narudzbi = (
        db.query(func.count(func.distinct(Narudzba.id)))
        .filter(Narudzba.korisnik_id == kupac.id)
        .scalar() or 0
    )

   
    opg_fav = (
        db.query(
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
            KorisnickiProfil.slika_profila.label("opg_slika"),
            func.count(NarudzbaStavka.id).label("broj")
        )
        .join(NarudzbaStavka, NarudzbaStavka.opg_id == Opg.id)
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Narudzba.korisnik_id == kupac.id)
        .group_by(Opg.id, Opg.naziv, Opg.slug, KorisnickiProfil.slika_profila)
        .order_by(desc("broj"))
        .first()
    )
    opg_favorit = None
    if opg_fav:
        opg_favorit = {
            "naziv": opg_fav.opg_naziv,
            "slug": opg_fav.opg_slug,
            "slika": opg_fav.opg_slika,
        }

   
    naj_proiz = (
        db.query(
            Proizvod.id,
            Proizvod.naziv,
            Proizvod.slug.label("proizvod_slug"),
            KategorijaProizvoda.slug.label("kat_slug"),
            func.sum(NarudzbaStavka.kolicina).label("kolicina_ukupno")
        )
        .join(NarudzbaStavka, NarudzbaStavka.proizvod_id == Proizvod.id)
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .join(KategorijaProizvoda, KategorijaProizvoda.id == Proizvod.kategorija_id)
        .filter(
            Narudzba.korisnik_id == kupac.id,
            NarudzbaStavka.tip == "proizvod",
        )
        .group_by(Proizvod.id, Proizvod.naziv, Proizvod.slug, KategorijaProizvoda.slug)
        .order_by(desc("kolicina_ukupno"))
        .first()
    )
    najcesci_proizvod = None
    if naj_proiz:
        najcesci_proizvod = {
            "id": naj_proiz.id,
            "naziv": naj_proiz.naziv,
            "kat_slug": naj_proiz.kat_slug,
            "proizvod_slug_id": f"{naj_proiz.proizvod_slug}-{naj_proiz.id}",
        }

   
    naj_usl = (
        db.query(
            Usluga.id,
            Usluga.naziv,
            Usluga.slug.label("usluga_slug"),
            KategorijaUsluge.slug.label("kat_slug"),
            func.sum(NarudzbaStavka.kolicina).label("kolicina_ukupno")
        )
        .join(NarudzbaStavka, NarudzbaStavka.usluga_id == Usluga.id)
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .join(KategorijaUsluge, KategorijaUsluge.id == Usluga.kategorija_id)
        .filter(
            Narudzba.korisnik_id == kupac.id,
            NarudzbaStavka.tip == "usluga",
        )
        .group_by(Usluga.id, Usluga.naziv, Usluga.slug, KategorijaUsluge.slug)
        .order_by(desc("kolicina_ukupno"))
        .first()
    )
    najcesca_usluga = None
    if naj_usl:
        najcesca_usluga = {
            "id": naj_usl.id,
            "naziv": naj_usl.naziv,
           
            "usluga_slug_id": f"{naj_usl.usluga_slug}-{naj_usl.id}",
        }

   
    zadnji_proizvodi = (
        db.query(
            NarudzbaStavka.id.label("stavka_id"),
            Narudzba.id.label("narudzba_id"),
            Narudzba.datum_izrade,
            NarudzbaStavka.naziv,
            NarudzbaStavka.slika,
            NarudzbaStavka.kolicina,
            NarudzbaStavka.mjerna_jedinica,
            NarudzbaStavka.cijena,
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
            KorisnickiProfil.slika_profila.label("opg_slika"),
        )
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .join(Opg, Opg.id == NarudzbaStavka.opg_id)
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(
            Narudzba.korisnik_id == kupac.id,
            NarudzbaStavka.tip == "proizvod",
        )
        .order_by(desc(Narudzba.datum_izrade), desc(NarudzbaStavka.id))
        .limit(3)
        .all()
    )

  
    zadnje_usluge = (
        db.query(
            NarudzbaStavka.id.label("stavka_id"),
            Narudzba.id.label("narudzba_id"),
            Narudzba.datum_izrade,
            NarudzbaStavka.naziv,
            NarudzbaStavka.slika,
            NarudzbaStavka.kolicina,
            NarudzbaStavka.mjerna_jedinica,
            NarudzbaStavka.cijena,
            Opg.naziv.label("opg_naziv"),
            Opg.slug.label("opg_slug"),
            KorisnickiProfil.slika_profila.label("opg_slika"),
        )
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .join(Opg, Opg.id == NarudzbaStavka.opg_id)
        .join(Korisnik, Korisnik.id == Opg.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(
            Narudzba.korisnik_id == kupac.id,
            NarudzbaStavka.tip == "usluga",
        )
        .order_by(desc(Narudzba.datum_izrade), desc(NarudzbaStavka.id))
        .limit(3)
        .all()
    )

    def map_stavka(s):
        return {
            "stavka_id": s.stavka_id,
            "narudzba_id": s.narudzba_id,  
            "datum_izrade": s.datum_izrade.isoformat() if s.datum_izrade else None,
            "naziv": s.naziv,
            "slika": s.slika,
            "kolicina": int(s.kolicina or 0),
            "mjerna_jedinica": s.mjerna_jedinica,
            "cijena": float(s.cijena or 0.0),
            "opg_naziv": s.opg_naziv,
            "opg_slug": s.opg_slug,
            "opg_slika": s.opg_slika,  
        }

    posljednje = {
        "proizvodi": [map_stavka(s) for s in zadnji_proizvodi],
        "usluge": [map_stavka(s) for s in zadnje_usluge],
    }

    statistika = {
        "ukupno_narudzbi": int(ukupno_narudzbi),
        "opg_favorit": opg_favorit,
        "najcesci_proizvod": najcesci_proizvod,
        "najcesca_usluga": najcesca_usluga,
    }

    return {"statistika": statistika, "posljednje": posljednje}