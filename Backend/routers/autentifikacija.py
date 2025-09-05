from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
from security import hashiranje_lozinke, kreiranje_tokena_za_pristup
from utils import slugify
from models import TipKorisnika, Korisnik, Kupac, KorisnickiProfil
from typing import Annotated
from security import verifikacija_lozinke

router = APIRouter(prefix="/autentifikacija", tags=["autentifikacija"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/registracija/kupac", response_model=schemas.Token, status_code=201)
def registracija_kupca(body: schemas.RegistracijaKupac, db: db_dependency):
    if body.lozinka != body.potvrda_lozinke:
        raise HTTPException(status_code=400, detail="Lozinke se ne podudaraju.")
    if db.query(Korisnik).filter(Korisnik.email == body.email).first():
        raise HTTPException(status_code=409, detail="Email je već registriran.")
    if db.query(Korisnik).filter(Korisnik.korisnicko_ime == body.korisnicko_ime).first():
        raise HTTPException(status_code=409, detail="Korisničko ime je zauzeto.")
    
    korisnik_kupac = Korisnik(
        email = body.email,
        korisnicko_ime = body.korisnicko_ime,
        lozinka = hashiranje_lozinke(body.lozinka),
        ime = body.ime,
        prezime = body.prezime,
        tip_korisnika = TipKorisnika.kupac,
    )

    db.add(korisnik_kupac)
    db.flush()

    korisnicki_profil_kupca = KorisnickiProfil(korisnik_id = korisnik_kupac.id)
    db.add(korisnicki_profil_kupca)

    slug = slugify(body.korisnicko_ime)

    kupac = Kupac(korisnik_id = korisnik_kupac.id, slug=slug)
    db.add(kupac)

    db.commit()

    token = kreiranje_tokena_za_pristup(korisnik_kupac.id)
    return {"access_token": token, "token_type": "bearer"}
    

@router.post("/prijava", response_model=schemas.Token)
def prijava(body: schemas.Prijava, db: db_dependency):
    korisnik = (
        db.query(Korisnik).filter(
            (Korisnik.email == body.email_ili_korisnicko_ime) | (Korisnik.korisnicko_ime == body.email_ili_korisnicko_ime)
            ).first()
    )

    if not korisnik:
        raise HTTPException(status_code=401, detail="Neispravni podaci za prijavu")
    
    if not verifikacija_lozinke(body.lozinka, korisnik.lozinka):
        raise HTTPException(status_code=401, detail="Neispravni podaci za prijavu")
    
    token = kreiranje_tokena_za_pristup(korisnik.id)
    return {"access_token": token, "token_type": "bearer"}