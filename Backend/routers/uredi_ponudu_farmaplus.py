from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from sqlalchemy import func, case
from typing import List, Dict, Any
from models import Usluga, KategorijaUsluge, Opg, Korisnik, TipKorisnika
from schemas import KreiranjeUsluge, AzuriranjeUsluge, PrikazUsluge
from security import dohvati_id_trenutnog_korisnika
import os
from datetime import datetime
from utils import obrisi_uploadanu_sliku

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/opg/ponuda-farmaplus", tags=["OPG ponuda usluga"])

def opg_ili_404(db: Session, korisnik_id: int) -> Opg:
    opg = db.query(Opg).filter(Opg.korisnik_id == korisnik_id).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    return opg

@router.get("/kategorije", response_model=List[Dict[str, Any]])
def kategorije_usluga(
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)

    kategorije_s_brojacem = (
        db.query(
            KategorijaUsluge.id,
            KategorijaUsluge.naziv,
            KategorijaUsluge.slug,
            func.count(Usluga.id).label("ukupno"),
            func.sum(
                case(
                    (Usluga.usluga_dostupna == False, 1),
                    else_=0
                )
            ).label("nedostupni"),
            func.sum(case(
                (Usluga.usluga_dostupna == True, 1),
                else_=0
            )).label("dostupni")
        ).outerjoin(
            Usluga,
            (Usluga.kategorija_id == KategorijaUsluge.id) & 
            (Usluga.opg_id == opg.id) 
        ).group_by(KategorijaUsluge.id, KategorijaUsluge.naziv, KategorijaUsluge.slug).order_by(KategorijaUsluge.naziv.asc()).all()
    )
    return [{"id": kategorija.id, "naziv": kategorija.naziv, "slug": kategorija.slug, "ukupno": int(kategorija.ukupno or 0), "nedostupni": int(kategorija.nedostupni or 0), "dostupni": int(kategorija.dostupni or 0)} for kategorija in kategorije_s_brojacem]


@router.get("", response_model=List[PrikazUsluge])
def lista_usluga(
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    kategorija_id: int | None = None,
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    usluga = db.query(Usluga).filter(Usluga.opg_id == opg.id)
    if kategorija_id:
        usluga = usluga.filter(Usluga.kategorija_id == kategorija_id)
    return usluga.order_by(Usluga.datum_izrade.desc()).all() 


@router.post("", response_model=PrikazUsluge)
def kreiraj_uslugu(
    body: KreiranjeUsluge,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    if not db.get(KategorijaUsluge, body.kategorija_id):
        raise HTTPException(status_code=404, detail="Kategorija ne postoji")
    
    usluga = Usluga(
        naziv = body.naziv,
        opis = body.opis,
        cijena = body.cijena,
        mjerna_jedinica = body.mjerna_jedinica,
        usluga_dostupna = body.usluga_dostupna,
        kategorija_id = body.kategorija_id,
        opg_id = opg.id,
        slug = f"{opg.id}-{body.naziv.lower().replace(' ', '-')}",
        slika_usluge = body.slika_usluge

    )
    db.add(usluga)
    db.commit()
    db.refresh(usluga)
    return usluga


@router.put("/{usluga_id}", response_model=PrikazUsluge)
def uredi_uslugu(
    usluga_id: int,
    body: AzuriranjeUsluge,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    usluga = db.get(Usluga, usluga_id)
    if not usluga or usluga.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Usluga nije pronađena")
    
    for p in ["naziv", "opis", "cijena", "slika_usluge", "usluga_dostupna", "mjerna_jedinica", "kategorija_id"]:
         val = getattr(body, p, None)
         if val is not None:
             setattr(usluga, p, val)
    db.commit()
    db.refresh(usluga)
    return usluga

@router.delete("/{usluga_id}", status_code=204)
def obrisi_uslugu(
    usluga_id: int,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    usluga = db.get(Usluga, usluga_id)
    if not usluga or usluga.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Usluga nije pronađena")
    
    if usluga.slika_usluge:
        obrisi_uploadanu_sliku(usluga.slika_usluge)
    
    db.delete(usluga)
    db.commit()
    return

@router.post("/{usluga_id}/slika", response_model=PrikazUsluge)
def ucitaj_sliku_usluge(
    request: Request,
    usluga_id: int,
    slika_usluge: UploadFile = File(...),
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    trenutno_vrijeme = datetime.now().strftime("%H%M%S%f")
    opg = opg_ili_404(db, id_korisnika)
    usluga = db.get(Usluga, usluga_id)
    if not usluga or usluga.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Usluga nije pronađena")
    
    if usluga.slika_usluge:
        obrisi_uploadanu_sliku(usluga.slika_usluge)

    os.makedirs("static/uploads", exist_ok=True)
    ekstenzija = os.path.splitext(slika_usluge.filename)[1].lower() or ".jpg"
    naziv_slike = f"usluga_{usluga.id}_{trenutno_vrijeme}{ekstenzija}"
    path = os.path.join("static", "uploads", naziv_slike)

    with open(path, "wb") as f:
        f.write(slika_usluge.file.read())

    url = request.url_for("static", path=f"uploads/{naziv_slike}")

    usluga.slika_usluge = str(url)
    db.commit()
    db.refresh(usluga)
    return usluga 