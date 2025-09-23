from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import SessionLocal
from models import KosaricaStavka, Proizvod, Usluga, Opg
from schemas import KosaricaDodajProizvod, KosaricaDodajUslugu, KosaricaPromijeniKolicinu, KosaricaStavkaPrikaz, KosaricaPrikaz
from security import dohvati_id_trenutnog_korisnika

router = APIRouter(prefix="/kosarica", tags=["Košarica"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _map_stavka(s: KosaricaStavka) -> KosaricaStavkaPrikaz:
    tip = "proizvod" if s.proizvod_id else "usluga"
    naziv = s.proizvod.naziv if s.proizvod_id else s.usluga.naziv
    slika = (s.proizvod.slika_proizvoda if s.proizvod_id else s.usluga.slika_usluge) if (s.proizvod_id or s.usluga_id) else None
    opg = s.proizvod.opg if s.proizvod_id else s.usluga.opg
    opg_naziv = opg.naziv if opg else None
    opg_slug = opg.slug if opg else None

    return KosaricaStavkaPrikaz(
        id = s.id,
        tip = tip,
        proizvod_id = s.proizvod_id,
        usluga_id = s.usluga_id,
        naziv = naziv,
        slika = slika,
        opg_naziv = opg_naziv,
        opg_slug = opg_slug,
        cijena = s.cijena,
        mjerna_jedinica = s.mjerna_jedinica,
        kolicina = s.kolicina,
        termin_od = s.termin_od,
        termin_do = s.termin_do,
    )


@router.get("", response_model=KosaricaPrikaz)
def dohvati_kosaricu(db: Session = Depends(get_db), korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika)):
    kosarica = (
        db.query(KosaricaStavka)
        .options(joinedload(KosaricaStavka.proizvod).joinedload(Proizvod.opg))
        .options(joinedload(KosaricaStavka.usluga).joinedload(Usluga.opg))
        .filter(KosaricaStavka.korisnik_id == korisnik_id)
        .all()
    )
    return {"stavke": [_map_stavka(s) for s in kosarica]}


@router.post("/proizvodi", response_model=KosaricaPrikaz)
def dodaj_proizvod(
    body: KosaricaDodajProizvod,
    db: Session = Depends(get_db),
    korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika),
):
    p = db.query(Proizvod).filter(Proizvod.id == body.proizvod_id).first()
    if not p:
        raise HTTPException(404, "Proizvod nije pronađen")
    if not p.proizvod_dostupan:
        raise HTTPException(400, "Proizvod nije dostupan")
    
    s = (
        db.query(KosaricaStavka)
        .filter(
            KosaricaStavka.korisnik_id == korisnik_id,
            KosaricaStavka.proizvod_id == p.id,
        ).first()
    )

    if s:
        s.kolicina += int(body.kolicina)
        s.cijena = p.cijena
        s.mjerna_jedinica = p.mjerna_jedinica
    else:
        s = KosaricaStavka(
            korisnik_id = korisnik_id,
            proizvod_id = p.id,
            kolicina = int(body.kolicina),
            termin_od = None,
            termin_do = None,
            cijena = p.cijena,
            mjerna_jedinica = p.mjerna_jedinica,
        )
        db.add(s)
    
    db.commit()
    return dohvati_kosaricu(db, korisnik_id)


@router.post("/usluge", response_model=KosaricaPrikaz)
def dodaj_uslugu(
    body: KosaricaDodajUslugu,
    db: Session = Depends(get_db),
    korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika),
):
    u = db.query(Usluga).filter(Usluga.id == body.usluga_id).first()

    if not u:
        raise HTTPException(404, "Usluga nije pronađena")
    if not u.usluga_dostupna:
        raise HTTPException(400, "Usluga nije dostupna")
    
    s = (
        db.query(KosaricaStavka)
        .filter(
            KosaricaStavka.korisnik_id == korisnik_id,
            KosaricaStavka.usluga_id == u.id,
            KosaricaStavka.termin_od.is_(body.termin_od if body.termin_od is None else None) if False else None
        ).first()
    )

    if body.termin_od and body.termin_do:
        s = (
            db.query(KosaricaStavka)
            .filter(
                KosaricaStavka.korisnik_id == korisnik_id,
                KosaricaStavka.usluga_id == u.id,
                KosaricaStavka.termin_od == body.termin_od,
                KosaricaStavka.termin_do == body.termin_do
            ).first()
        )
    else:
        s = (
            db.query(KosaricaStavka)
            .filter(
                KosaricaStavka.korisnik_id == korisnik_id,
                KosaricaStavka.usluga_id == u.id,
                KosaricaStavka.termin_od.is_(None),
                KosaricaStavka.termin_do.is_(None)
            ).first()
        )

    if s:
        s.kolicina += int(body.kolicina)
        s.cijena = u.cijena
        s.mjerna_jedinica = u.mjerna_jedinica
    else:
        s = KosaricaStavka(
            korisnik_id = korisnik_id,
            usluga_id = u.id,
            kolicina = int(body.kolicina),
            termin_od = body.termin_od,
            termin_do = body.termin_do,
            cijena = u.cijena,
            mjerna_jedinica = u.mjerna_jedinica
        )
        db.add(s)
    
    db.commit()
    return dohvati_kosaricu(db, korisnik_id)


@router.patch("/stavke/{stavka_id}", response_model=KosaricaPrikaz)
def promijeni_kolicinu(
    stavka_id:int,
    body: KosaricaPromijeniKolicinu,
    db: Session = Depends(get_db),
    korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika),
):
    s = (
        db.query(KosaricaStavka)
        .filter(KosaricaStavka.id == stavka_id, KosaricaStavka.korisnik_id == korisnik_id)
        .first()
    )

    if not s:
        raise HTTPException(404, "Stavka nije pronađena")
    
    if s.usluga_id and s.termin_od and s.termin_do:
        raise HTTPException(400, "Količina se ne može mijenjati za uslugu s terminom")
    
    s.kolicina = int(body.kolicina)
    db.commit()
    return dohvati_kosaricu(db, korisnik_id)


@router.delete("/stavke/{stavka_id}", response_model=KosaricaPrikaz)
def ukloni_stavku(
    stavka_id: int,
    db: Session = Depends(get_db),
    korisnik_id: int = Depends(dohvati_id_trenutnog_korisnika),
):
    s = (
        db.query(KosaricaStavka)
        .filter(KosaricaStavka.id == stavka_id, KosaricaStavka.korisnik_id == korisnik_id)
        .first()
    )
    if not s:
        raise HTTPException(404, "Stavka nije pronađena")
    db.delete(s)
    db.commit()
    return dohvati_kosaricu(db, korisnik_id)