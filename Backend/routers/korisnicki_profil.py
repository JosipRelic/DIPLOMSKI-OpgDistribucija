import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Request, Response
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Korisnik, KorisnickiProfil, Opg, Kupac, TipKorisnika, KosaricaStavka, Narudzba
from security import dohvati_id_trenutnog_korisnika
import schemas
from typing import Annotated
from utils import obrisi_uploadanu_sliku
from datetime import datetime
from models import Recenzija
from sqlalchemy import func, distinct

router = APIRouter(prefix="/profil", tags=["Korisnički profil"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def _ponovno_izracunaj_prosjek_ocjene(db, opg_id: int):
    prosjecna_ocjena, broj_recenzija = (
        db.query(func.avg(Recenzija.ocjena), func.count(Recenzija.id)).filter(Recenzija.opg_id == opg_id).first()
    )
    opg = db.query(Opg).get(opg_id)
    if opg:
        opg.prosjecna_ocjena = float(prosjecna_ocjena) if prosjecna_ocjena is not None else None
        opg.broj_recenzija = int(broj_recenzija or 0)



def _serialize_me(korisnik: Korisnik) -> schemas.PrikazKorisnickogProfila:
    profil = korisnik.korisnicki_profil
    base = dict(
        id = korisnik.id,
        email = korisnik.email,
        ime = korisnik.ime,
        prezime = korisnik.prezime,
        tip_korisnika = korisnik.tip_korisnika.value,
        broj_telefona = korisnik.broj_telefona,
        slika_profila = profil.slika_profila if profil else None,
        drzava = profil.drzava if profil else None,
        zupanija = profil.zupanija if profil else None,
        grad = profil.grad if profil else None,
        postanski_broj = profil.postanski_broj if profil else None,
        adresa = profil.adresa if profil else None,
        slug = None,
        naziv = None,
        opis = None,
        identifikacijski_broj_mibpg = None,           
    )

    if korisnik.tip_korisnika == TipKorisnika.kupac:
        kupac = korisnik.kupac
        if kupac:
            base["slug"] = kupac.slug

    if korisnik.tip_korisnika == TipKorisnika.opg:
        opg = korisnik.opg
        if opg:
            base.update(
                naziv = opg.naziv,
                opis = opg.opis,
                identifikacijski_broj_mibpg = opg.identifikacijski_broj_mibpg,
                slug = opg.slug
            )

    return schemas.PrikazKorisnickogProfila(**base)

@router.get("/moj-profil", response_model=schemas.PrikazKorisnickogProfila)
def dohvati_profil(
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
    ):
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    if not korisnik:
        raise HTTPException(status_code=404, detail="Korisnik ne postoji")
    return _serialize_me(korisnik)
    

@router.put("", response_model=schemas.PrikazKorisnickogProfila)
def azuriraj_profil(
    body: schemas.AzuriranjeKorisnickogProfila,
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
    
):
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    if not korisnik:
        raise HTTPException(status_code=404, detail="Korisnik ne postoji")

    for f in ["email", "ime", "prezime", "broj_telefona"]:
        val = getattr(body, f)
        if val is not None:
            setattr(korisnik, f, val)

    korisnicki_profil = korisnik.korisnicki_profil
    if not korisnicki_profil:
        korisnicki_profil = KorisnickiProfil(korisnik_id = korisnik.id)
        db.add(korisnicki_profil)
        db.flush()

    for f in ["drzava", "zupanija", "grad", "postanski_broj", "adresa"]:
        val = getattr(body, f)
        if val is not None:
            setattr(korisnicki_profil, f, val)

    
    if korisnik.tip_korisnika == TipKorisnika.kupac:
        kupac = korisnik.kupac
        if kupac and body.slug is not None:
            slug_postoji_kupac = db.query(Kupac).filter(
                Kupac.slug == body.slug,
                Kupac.id != kupac.id
            ).first()
            if slug_postoji_kupac:
                raise HTTPException(status_code=409, detail="Slug je već zauzet.")
            kupac.slug = body.slug
    
    elif korisnik.tip_korisnika == TipKorisnika.opg:
        opg = korisnik.opg      
        if not opg:
            opg = Opg(
                korisnik_id = korisnik.id,
                naziv = "",
                opis = "",
                identifikacijski_broj_mibpg="",
                slug =f"opg-{korisnik.id}"
            )  
            db.add(opg)
            db.flush()

        if body.naziv is not None:
            opg.naziv = body.naziv
        if body.opis is not None:
            opg.opis = body.opis
        if body.identifikacijski_broj_mibpg is not None:
            mibpg_postoji = db.query(Opg).filter(
                Opg.identifikacijski_broj_mibpg == body.identifikacijski_broj_mibpg,
                Opg.id != opg.id
            ).first()
            if mibpg_postoji:
                raise HTTPException(status_code=409, detail="MIBPG je već registriran pod tim brojem.")
            opg.identifikacijski_broj_mibpg = body.identifikacijski_broj_mibpg
            
        if body.slug is not None:
            slug_postoji_opg = db.query(Opg).filter(
                Opg.slug == body.slug,
                Opg.id != opg.id
            ).first()
            if slug_postoji_opg:
                raise HTTPException(status_code=409, detail="Slug je već zauzet.")
            opg.slug = body.slug
    
    db.commit()
    db.refresh(korisnik)
    return _serialize_me(korisnik)


@router.post("/slika-profila", response_model=schemas.PrikazKorisnickogProfila)
def ucitaj_sliku_profila(
    request: Request,
    slika: UploadFile = File(...),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db),

):
    trenutno_vrijeme = datetime.now().strftime("%H%M%S%f")
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    if not korisnik:
        raise HTTPException(status_code=404, detail="Korisnik ne postoji")
    
    if korisnik.korisnicki_profil and korisnik.korisnicki_profil.slika_profila:
        obrisi_uploadanu_sliku(korisnik.korisnicki_profil.slika_profila)

    os.makedirs("static/uploads", exist_ok=True)
    ekstenzija = os.path.splitext(slika.filename)[1].lower() or ".jpg"
    naziv_slike = f"korisnik_{korisnik.id}_{trenutno_vrijeme}{ekstenzija}"
    path = os.path.join("static", "uploads", naziv_slike)

    with open(path, "wb") as f:
        f.write(slika.file.read())

    url = request.url_for("static", path=f"uploads/{naziv_slike}")

    korisnicki_profil = korisnik.korisnicki_profil or KorisnickiProfil(korisnik_id = korisnik.id)
    db.add(korisnicki_profil)

    korisnicki_profil.slika_profila = str(url)
    db.commit()
    
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    return _serialize_me(korisnik) 

@router.delete("", status_code=204)
def obrisi_profil(
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    if not korisnik:
        raise HTTPException(status_code=404, detail="Korisnik ne postoji")
    
    utjece_na_opgove = [
        oid for (oid, ) in db.query(distinct(Recenzija.opg_id)).filter(Recenzija.korisnik_id == id_trenutnog_korisnika).all()
    ]
    
    if korisnik.korisnicki_profil and korisnik.korisnicki_profil.slika_profila:
        obrisi_uploadanu_sliku(korisnik.korisnicki_profil.slika_profila)
    

    db.query(KosaricaStavka).filter(KosaricaStavka.korisnik_id == id_trenutnog_korisnika).delete(synchronize_session=False)

    db.delete(korisnik)
    db.flush()

    for opg_id in utjece_na_opgove:
        _ponovno_izracunaj_prosjek_ocjene(db, opg_id)

    db.commit()
    return {"detalji": "Profil obrisan."}