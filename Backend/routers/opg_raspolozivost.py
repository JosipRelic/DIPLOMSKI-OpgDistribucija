from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict
from datetime import date, datetime, timedelta
from models import Opg, OpgRaspolozivostPoDatumu
from schemas import  DatumRaspolozivosti, DatumRapolozivostiPrikaz, MjeseciKalendaraPrikaz
from security import dohvati_id_trenutnog_korisnika
from database import SessionLocal

router = APIRouter(prefix="/opg/raspolozivost", tags=["OPG - Raspoloživost"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def opg_ili_404(db:Session, korisnik_id: int) -> Opg:
    opg = db.query(Opg).filter(Opg.korisnik_id == korisnik_id).first()
    if not opg: raise HTTPException(status_code=404, detail="OPG nije pronađen")
    return opg

def hhmm_u_minute(hhmm: str) -> int:
    sati, minute = map(int, hhmm.split(":"))
    return sati*60 + minute

def minute_u_hhmm(v: int) -> str:
    sati, minute = divmod(max(0, v), 60)
    return f"{sati:02d}:{minute:02d}"



@router.get("/dani", response_model=List[DatumRapolozivostiPrikaz])
def dohvati_dane(
    godina: int = Query(..., ge=2000, le=2100),
    mjesec: int = Query(..., ge=1, le=12),
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    pocetak = date(godina, mjesec, 1)

    if mjesec == 12: 
        kraj = date(godina+1, 1, 1) - timedelta(days=1)
    else: 
        kraj = date(godina, mjesec+1, 1) - timedelta(days=1)

    dani = (
        db.query(OpgRaspolozivostPoDatumu)
        .filter(OpgRaspolozivostPoDatumu.opg_id == opg.id, OpgRaspolozivostPoDatumu.datum >= pocetak, OpgRaspolozivostPoDatumu.datum <= kraj)
        .order_by(OpgRaspolozivostPoDatumu.datum.asc(), OpgRaspolozivostPoDatumu.pocetno_vrijeme.asc())
        .all()
    )
    return [
        DatumRapolozivostiPrikaz(
            id = dan.id, 
            datum = dan.datum,
            pocetno_vrijeme = minute_u_hhmm(dan.pocetno_vrijeme),
            zavrsno_vrijeme = minute_u_hhmm(dan.zavrsno_vrijeme),
            naslov = dan.naslov
        ) for dan in dani
    ]


@router.post("/dani", response_model=DatumRapolozivostiPrikaz, status_code=201)
def dodaj_dan(
        body: DatumRaspolozivosti,
        id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
        db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    pocetno_vrijeme = hhmm_u_minute(body.pocetno_vrijeme)
    zavrsno_vrijeme = hhmm_u_minute(body.zavrsno_vrijeme)

    if pocetno_vrijeme >= zavrsno_vrijeme:
        raise HTTPException(status_code=400, detail="Završno vrijeme mora biti veće od početnog")
    if datetime.combine(body.datum, datetime.min.time()) < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        raise HTTPException(status_code=400, detail="Datum je u prošlosti")
    
    preklapanje = (
        db.query(OpgRaspolozivostPoDatumu)
        .filter(
            OpgRaspolozivostPoDatumu.opg_id == opg.id,
            OpgRaspolozivostPoDatumu.datum == body.datum,
            OpgRaspolozivostPoDatumu.pocetno_vrijeme < zavrsno_vrijeme,
            OpgRaspolozivostPoDatumu.zavrsno_vrijeme > pocetno_vrijeme,
            ).first()
    )

    if preklapanje:
        raise HTTPException(status_code=409, detail="Raspon se preklapa s postojećim terminom.")

    dan = OpgRaspolozivostPoDatumu(opg_id = opg.id, datum = body.datum, pocetno_vrijeme = pocetno_vrijeme, zavrsno_vrijeme = zavrsno_vrijeme, naslov = body.naslov)
    
    db.add(dan)
    db.commit()
    db.refresh(dan)
    
    return DatumRapolozivostiPrikaz(id = dan.id, datum = dan.datum, pocetno_vrijeme = body.pocetno_vrijeme, zavrsno_vrijeme = body.zavrsno_vrijeme, naslov = dan.naslov)


@router.put("/dani/{id}", response_model=DatumRapolozivostiPrikaz)
def uredi_dan(
    id: int,
    body: DatumRaspolozivosti,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    dan = db.query(OpgRaspolozivostPoDatumu).filter_by(id=id, opg_id=opg.id).first()

    if not dan:
        raise HTTPException(status_code=404, detail="Termin nije pronađen")
    
    pocetak = hhmm_u_minute(body.pocetno_vrijeme)
    zavrsetak = hhmm_u_minute(body.zavrsno_vrijeme)
    if pocetak >= zavrsetak:
        raise HTTPException(status_code=400, detail="Završno vrijeme mora biti veće od početnog")
    
    if datetime.combine(body.datum, datetime.min.time()) < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        raise HTTPException(status_code=400, detail="Datum je u prošlosti")
    
    preklapanje = (
        db.query(OpgRaspolozivostPoDatumu)
        .filter(
            OpgRaspolozivostPoDatumu.opg_id == opg.id,
            OpgRaspolozivostPoDatumu.datum == body.datum,
            OpgRaspolozivostPoDatumu.id != id,
            OpgRaspolozivostPoDatumu.pocetno_vrijeme < zavrsetak,
            OpgRaspolozivostPoDatumu.zavrsno_vrijeme > pocetak
        ).first()
    )

    if preklapanje:
        raise HTTPException(status_code=409, detail="Termin se preklapa s postojećim terminom")
    
    dan.datum = body.datum
    dan.pocetno_vrijeme = pocetak
    dan.zavrsno_vrijeme = zavrsetak
    dan.naslov = body.naslov
    db.commit()
    db.refresh(dan)

    return DatumRapolozivostiPrikaz(
        id = dan.id,
        datum = dan.datum,
        pocetno_vrijeme = minute_u_hhmm(dan.pocetno_vrijeme),
        zavrsno_vrijeme = minute_u_hhmm(dan.zavrsno_vrijeme),
        naslov = dan.naslov,
    )



@router.delete("/dani/{id}", status_code=204)
def obrisi_dan(
    id: int,
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    dan = db.query(OpgRaspolozivostPoDatumu).filter_by(id = id, opg_id = opg.id).first()
    
    if not dan:
        raise HTTPException(status_code=404, detail="Nema zapisa")
    
    db.delete(dan)
    db.commit()
    return


@router.get("/kalendar", response_model=MjeseciKalendaraPrikaz)
def kalendar_mjesec(
    opg_id: int = Query(..., ge=1),
    godina: int = Query(..., ge=2000, le=2100),
    mjesec: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db),
):
    pocetak = date(godina, mjesec, 1)
    
    if mjesec == 12:
        kraj = date(godina+1, 1, 1) - timedelta(days=1)
    else:
        kraj = date(godina, mjesec+1, 1) - timedelta(days=1)
    
 
    dnevno = db.query(OpgRaspolozivostPoDatumu).filter(
        OpgRaspolozivostPoDatumu.opg_id == opg_id,
        OpgRaspolozivostPoDatumu.datum >= pocetak,
        OpgRaspolozivostPoDatumu.datum <= kraj
    ).all()

    dani_po_datumu: Dict[date, list[tuple[int, int]]] = {}

    for dan in dnevno:
        dani_po_datumu.setdefault(dan.datum, []).append((dan.pocetno_vrijeme, dan.zavrsno_vrijeme))

    slotovi: Dict[str, list[tuple[str, str]]] = {}
    d = pocetak

    while d <= kraj:
        key = d.isoformat()
        raspon = []

        if d in dani_po_datumu:
            for p, k in sorted(dani_po_datumu[d]):
                raspon.append( (minute_u_hhmm(p), minute_u_hhmm(k)) )
       
    
        
        if raspon:
            slotovi[key] = raspon
        
        d += timedelta(days=1)

    return MjeseciKalendaraPrikaz(slotovi=slotovi)

