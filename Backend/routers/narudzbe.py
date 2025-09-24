from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from security import SessionLocal, dohvati_id_trenutnog_korisnika
from datetime import datetime
import time
from uuid import uuid4
from models import Narudzba, NarudzbaStavka, KosaricaStavka
from schemas import NarudzbaKreiranje, NarudzbaPrikaz


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
        stavka = NarudzbaStavka(
            tip = s.tip,
            naziv = s.naziv,
            kolicina = s.kolicina,
            mjerna_jedinica = s.mjerna_jedinica,
            cijena = s.cijena,
            slika = s.slika,
            termin_od = s.termin_od,
            termin_do = s.termin_do,
        )
        narudzba.stavke.append(stavka)
    
    db.add(narudzba)
    db.flush()

    db.query(KosaricaStavka).filter(KosaricaStavka.korisnik_id == korisnik_id).delete(synchronize_session=False)

    db.commit()
    db.refresh(narudzba)

    return narudzba
