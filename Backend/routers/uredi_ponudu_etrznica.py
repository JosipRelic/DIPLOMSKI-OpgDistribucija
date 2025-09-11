from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from sqlalchemy import func, case
from typing import List, Dict, Any
from models import Proizvod, KategorijaProizvoda, Opg, Korisnik, TipKorisnika
from schemas import KreiranjeProizvoda, AzuriranjeProizvoda, PrikazProizvoda
from security import dohvati_id_trenutnog_korisnika
import os

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/opg/ponuda-etrznica", tags=["OPG ponuda proizvoda"])

def opg_ili_404(db: Session, korisnik_id: int) -> Opg:
    opg = db.query(Opg).filter(Opg.korisnik_id == korisnik_id).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    return opg

@router.get("/kategorije", response_model=List[Dict[str, Any]])
def kategorije(
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)

    kategorije_s_brojacem = (
        db.query(
            KategorijaProizvoda.id,
            KategorijaProizvoda.naziv,
            KategorijaProizvoda.slug,
            func.count(Proizvod.id).label("ukupno"),
            func.sum(
                case(
                    (Proizvod.proizvod_dostupan == False, 1),
                    else_=0
                )
            ).label("nedostupni"),
            func.sum(case(
                (Proizvod.proizvod_dostupan == True, 1),
                else_=0
            )).label("dostupni")
        ).outerjoin(
            Proizvod,
            (Proizvod.kategorija_id == KategorijaProizvoda.id) & 
            (Proizvod.opg_id == opg.id) 
        ).group_by(KategorijaProizvoda.id, KategorijaProizvoda.naziv, KategorijaProizvoda.slug).order_by(KategorijaProizvoda.naziv.asc()).all()
    )
    return [{"id": kategorija.id, "naziv": kategorija.naziv, "slug": kategorija.slug, "ukupno": int(kategorija.ukupno or 0), "nedostupni": int(kategorija.nedostupni or 0), "dostupni": int(kategorija.dostupni or 0)} for kategorija in kategorije_s_brojacem]

@router.get("", response_model=List[PrikazProizvoda])
def lista_proizvoda(
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    kategorija_id: int | None = None,
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    proizvod = db.query(Proizvod).filter(Proizvod.opg_id == opg.id)
    if kategorija_id:
        proizvod = proizvod.filter(Proizvod.kategorija_id == kategorija_id)
    return proizvod.order_by(Proizvod.datum_izrade.desc()).all() 


@router.post("", response_model=PrikazProizvoda)
def kreiraj_proizvod(
    body: KreiranjeProizvoda,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    if not db.get(KategorijaProizvoda, body.kategorija_id):
        raise HTTPException(status_code=404, detail="Kategorija ne postoji")
    
    proizvod = Proizvod(
        naziv = body.naziv,
        opis = body.opis,
        cijena = body.cijena,
        mjerna_jedinica = body.mjerna_jedinica,
        proizvod_dostupan = body.proizvod_dostupan,
        kategorija_id = body.kategorija_id,
        opg_id = opg.id,
        slug = f"{opg.id}-{body.naziv.lower().replace(' ', '-')}",
        slika_proizvoda = body.slika_proizvoda

    )
    db.add(proizvod)
    db.commit()
    db.refresh(proizvod)
    return proizvod

@router.put("/{proizvod_id}", response_model=PrikazProizvoda)
def uredi_proizvod(
    proizvod_id: int,
    body: AzuriranjeProizvoda,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    proizvod = db.get(Proizvod, proizvod_id)
    if not proizvod or proizvod.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen")
    
    for p in ["naziv", "opis", "cijena", "slika_proizvoda", "proizvod_dostupan", "mjerna_jedinica", "kategorija_id"]:
         val = getattr(body, p, None)
         if val is not None:
             setattr(proizvod, p, val)
    db.commit()
    db.refresh(proizvod)
    return proizvod


@router.delete("/{proizvod_id}", status_code=204)
def obrisi_proizvod(
    proizvod_id: int,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    proizvod = db.get(Proizvod, proizvod_id)
    if not proizvod or proizvod.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen")
    if proizvod.slika_proizvoda and proizvod.slika_proizvoda.startswith("/static/uploads/"):
        try:
            aps = os.path.join(os.path.dirname(__file__), proizvod.slika_proizvoda.lstrip("/"))
            if os.path.exists(aps):
                os.remove(aps)
        except Exception:
            pass
    
    db.delete(proizvod)
    db.commit()
    return


@router.post("/{proizvod_id}/slika", response_model=PrikazProizvoda)
def ucitaj_sliku_proizvoda(
    request: Request,
    proizvod_id: int,
    slika_proizvoda: UploadFile = File(...),
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    proizvod = db.get(Proizvod, proizvod_id)
    if not proizvod or proizvod.opg_id != opg.id:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen")
    
    os.makedirs("static/uploads", exist_ok=True)
    ekstenzija = os.path.splitext(slika_proizvoda.filename)[1].lower() or ".jpg"
    naziv_slike = f"proizvod_{proizvod.id}{ekstenzija}"
    path = os.path.join("static", "uploads", naziv_slike)

    with open(path, "wb") as f:
        f.write(slika_proizvoda.file.read())

    url = request.url_for("static", path=f"uploads/{naziv_slike}")

    proizvod.slika_proizvoda = str(url)
    db.commit()
    db.refresh(proizvod)
    return proizvod 
