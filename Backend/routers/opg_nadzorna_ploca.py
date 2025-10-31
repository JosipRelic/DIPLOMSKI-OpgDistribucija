from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal
from models import KategorijaProizvoda, Korisnik, Opg, Proizvod, Recenzija, KorisnickiProfil, Narudzba, NarudzbaStavka, Usluga
from security import dohvati_id_trenutnog_korisnika

router = APIRouter(prefix="/opg/nadzorna-ploca", tags=["OPG profil - Nadzorna ploča"])

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
def nadzorna_ploca(
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika)
):
    opg = _moj_opg(db, id_trenutnog_korisnika)

    prosjek = float(opg.prosjecna_ocjena or 0.0)
    broj_recenzija = int(opg.broj_recenzija or 0)

    zadnje_recenije = (
        db.query(Recenzija, KorisnickiProfil.slika_profila, Korisnik.ime, Korisnik.prezime)
        .join(Korisnik, Korisnik.id == Recenzija.korisnik_id)
        .outerjoin(KorisnickiProfil, KorisnickiProfil.korisnik_id == Korisnik.id)
        .filter(Recenzija.opg_id == opg.id)
        .order_by(desc(Recenzija.datum_izrade))
        .limit(5)
        .all()
    )

    ocjene = {
        "prosjek": prosjek,
        "broj_recenzija": broj_recenzija,
        "recenzirao": [
            {
                "slika": zr[1],
                "ime": (zr[2] or "").strip(),
                "prezime": (zr[3] or "").strip(),
            } for zr in zadnje_recenije
        ]
    }

    zadnje_narudzbe = (
        db.query(Narudzba)
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(NarudzbaStavka.opg_id == opg.id)
        .order_by(desc(Narudzba.datum_izrade))
        .distinct()
        .limit(3)
        .all()
    )

    prikaz_zadnjih_narudzbi = []
    for zn in zadnje_narudzbe:
        s_set = {
            s[0] for s in db.query(NarudzbaStavka.status)
            .filter(
                NarudzbaStavka.narudzba_id == zn.id,
                NarudzbaStavka.opg_id == opg.id
            ).all()
        }

        if "otkazano" in s_set:
            status = "otkazano"
        elif s_set and s_set == {"isporuceno"}:
            status = "isporuceno"
        else:
            status = "u_tijeku"
        
        broj_proizvoda = (
            db.query(func.coalesce(func.sum(NarudzbaStavka.kolicina), 0))
            .filter(
                NarudzbaStavka.narudzba_id == zn.id,
                NarudzbaStavka.opg_id == opg.id,
                NarudzbaStavka.tip == "proizvod",
            ).scalar() or 0
        )

        broj_usluga = (
            db.query(func.coalesce(func.sum(NarudzbaStavka.kolicina), 0))
            .filter(
                    NarudzbaStavka.narudzba_id == zn.id,
                    NarudzbaStavka.opg_id == opg.id,
                    NarudzbaStavka.tip == "usluga",
                    ).scalar() or 0
        )

        opg_ukupno = float((
            db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
            .filter(
                NarudzbaStavka.narudzba_id == zn.id,
                NarudzbaStavka.opg_id == opg.id,
            ).scalar()
        ) or 0.0)

        kupac_slika = None
        if zn.korisnik_id:
            prof = (
                db.query(KorisnickiProfil.slika_profila)
                .filter(KorisnickiProfil.korisnik_id == zn.korisnik_id)
                .first()
            )
            kupac_slika = prof[0] if prof else None

      
        iznos_proizvoda = float((
            db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
            .filter(
                NarudzbaStavka.narudzba_id == zn.id,
                NarudzbaStavka.opg_id == opg.id,
                NarudzbaStavka.tip == "proizvod",
            ).scalar()
        ) or 0.0)

        iznos_usluga = float((
            db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
            .filter(
                NarudzbaStavka.narudzba_id == zn.id,
                NarudzbaStavka.opg_id == opg.id,
                NarudzbaStavka.tip == "usluga",
            ).scalar()
        ) or 0.0)
        

        dostava = "Besplatna" if zn.nacin_dostave == "osobno" else "5.00 €"
        if zn.nacin_dostave == "dostava":
            opg_ukupno += 5.0
        
        prikaz_zadnjih_narudzbi.append({
            "id": zn.id,
            "broj_narudzbe": zn.broj_narudzbe,
            "kupac_ime": f"{(zn.ime or '').strip()} {(zn.prezime or '').strip()}".strip(),
            "kupac_slika": kupac_slika,
            "status": status,
            "broj_proizvoda": int(broj_proizvoda),
            "broj_usluga": int(broj_usluga),
            "iznos_proizvoda": round(iznos_proizvoda, 2),
            "iznos_usluga": round(iznos_usluga, 2),
            "dostava": dostava,
            "ukupno": round(opg_ukupno, 2),
            "datum_izrade": zn.datum_izrade.isoformat() if zn.datum_izrade else None,
        })

    
    ukupno_narudzbi = (
        db.query(func.count(func.distinct(Narudzba.id)))
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(NarudzbaStavka.opg_id == opg.id)
        .scalar() or 0
    )

    ukupna_zarada = float((
        db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .filter(NarudzbaStavka.opg_id == opg.id, NarudzbaStavka.status != "otkazano").scalar()
    ) or 0.0)

    dostave_ukupno = (
        db.query(func.count(func.distinct(Narudzba.id)))
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(NarudzbaStavka.opg_id == opg.id, NarudzbaStavka.status != "otkazano", Narudzba.nacin_dostave == "dostava").scalar() or 0
    )

    ukupna_zarada += dostave_ukupno * 5.0
    danas = date.today()
    pocetak_mjeseca = date(danas.year, danas.month, 1)
    if danas.month == 12:
        pocetak_slj_mjeseca = date(danas.year + 1, 1, 1)
    else:
        pocetak_slj_mjeseca = date(danas.year, danas.month + 1, 1)

    mjesecna_zarada = float((
        db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
        .join(Narudzba, Narudzba.id == NarudzbaStavka.narudzba_id)
        .filter(
            NarudzbaStavka.opg_id == opg.id,
            NarudzbaStavka.status != "otkazano",
            func.date(Narudzba.datum_izrade) >= pocetak_mjeseca,
            func.date(Narudzba.datum_izrade) < pocetak_slj_mjeseca,
        ).scalar()
    ) or 0.0)

    mjesecne_dostave = (
        db.query(func.count(func.distinct(Narudzba.id)))
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(
            NarudzbaStavka.opg_id == opg.id,
            NarudzbaStavka.status != "otkazano",
            Narudzba.nacin_dostave == "dostava",
            func.date(Narudzba.datum_izrade) >= pocetak_mjeseca,
            func.date(Narudzba.datum_izrade) < pocetak_slj_mjeseca,
        ).scalar() or 0
    )
    mjesecna_zarada += mjesecne_dostave * 5.0


    naj_pro = (
        db.query(
            NarudzbaStavka.proizvod_id.label("pid"),
            func.sum(NarudzbaStavka.kolicina).label("zbroj")
        )
        .filter(
            NarudzbaStavka.opg_id == opg.id,
            NarudzbaStavka.tip == "proizvod",
            NarudzbaStavka.status != "otkazano",
            NarudzbaStavka.proizvod_id.isnot(None),
        )
        .group_by(NarudzbaStavka.proizvod_id)
        .order_by(desc("zbroj"))
        .first()
        )
    
    najprodavaniji_proizvod = None
    if naj_pro and naj_pro.pid:    
        p = (
            db.query(Proizvod.slug, Proizvod.id, Proizvod.naziv, KategorijaProizvoda.slug.label("kat_slug"))
            .join(KategorijaProizvoda, KategorijaProizvoda.id == Proizvod.kategorija_id)
            .filter(Proizvod.id == naj_pro.pid)
            .first()
        )
        if p:
            najprodavaniji_proizvod = {
                "id": p.id,
                "slug": p.slug,
                "kategorija_slug": p.kat_slug,
                "naziv": p.naziv,
            }

    naj_usl = (
        db.query(
            NarudzbaStavka.usluga_id.label("uid"),
            func.sum(NarudzbaStavka.kolicina).label("zbroj")
        )
        .filter(
            NarudzbaStavka.opg_id == opg.id,
            NarudzbaStavka.tip == "usluga",
            NarudzbaStavka.status != "otkazano",
            NarudzbaStavka.usluga_id.isnot(None),
        )
        .group_by(NarudzbaStavka.usluga_id)
        .order_by(desc("zbroj"))
        .first()
    )

    najtrazenija_usluga = None

    if naj_usl and naj_usl.uid:
        u = (
            db.query(Usluga.slug, Usluga.id, Usluga.naziv)
            .filter(Usluga.id == naj_usl.uid)
            .first()
        )
        if u:
            najtrazenija_usluga = {
                "id": u.id,
                "slug": u.slug,
                "naziv": u.naziv,
            }

    naj_kupac = (
        db.query(
            Narudzba.korisnik_id,
            Narudzba.email, Narudzba.ime, Narudzba.prezime,
            func.count(func.distinct(Narudzba.id)).label("zbroj")
        )
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(NarudzbaStavka.opg_id == opg.id)
        .group_by(Narudzba.korisnik_id, Narudzba.email, Narudzba.ime, Narudzba.prezime)
        .order_by(desc("zbroj"))
        .first()
    )
    najvjerniji_kupac = None

    if naj_kupac:
        tip = None
        kupac_slug = None
        opg_slug = None
        if naj_kupac[0]: 
            k = db.get(Korisnik, naj_kupac[0])
            if k:
                tip = k.tip_korisnika.value  
                if k.kupac:
                    kupac_slug = k.kupac.slug
                if k.opg:
                    opg_slug = k.opg.slug
        najvjerniji_kupac = {
            "ime": (naj_kupac[2] or "").strip(),
            "prezime": (naj_kupac[3] or "").strip(),
            "email": naj_kupac[1],
            "broj_narudzbi": int(naj_kupac[4] or 0),
            "tip": tip,             
            "kupac_slug": kupac_slug,
            "opg_slug": opg_slug,
        }

    statistika = {
        "ukupno_narudzbi": int(ukupno_narudzbi),
        "zarada_ovaj_mjesec": round(mjesecna_zarada, 2),
        "zarada_ukupno": round(ukupna_zarada, 2),
        "najprodavaniji_proizvod": najprodavaniji_proizvod,
        "najvjerniji_kupac": najvjerniji_kupac,
        "najtrazenija_usluga": najtrazenija_usluga,
    }

    return {
        "ocjene": ocjene,
        "posljednje_narudzbe": prikaz_zadnjih_narudzbi,
        "statistika": statistika,
    }

