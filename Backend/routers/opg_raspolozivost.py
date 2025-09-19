from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict
from datetime import date, datetime, timedelta
from models import Opg, OpgTjednaRaspolozivost, OpgRaspolozivostPoDatumu
from schemas import TjednoPravilo, TjednoPraviloPrikaz, DatumRaspolozivosti, DatumRapolozivostiPrikaz, MjeseciKalendaraPrikaz
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

@router.get("/tjedno", response_model=List[TjednoPraviloPrikaz])
def dohvati_tjedna_pravila(
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)
    
    pravila = (
        db.query(OpgTjednaRaspolozivost)
        .filter(OpgTjednaRaspolozivost.opg_id == opg.id)
        .order_by(OpgTjednaRaspolozivost.dan_u_tjednu.asc())
        .all()
    )

    if not pravila:
        return [
            TjednoPraviloPrikaz(id=-(i+1), dan_u_tjednu=i, odabrano=False, pocetno_vrijeme="00:00", zavrsno_vrijeme="00:00", naslov=None)
            for i in range(7)
        ]
    return [
        TjednoPraviloPrikaz(
            id = pravilo.dan_u_tjednu,
            odabrano = pravilo.odabrano,
            pocetno_vrijeme = minute_u_hhmm(pravilo.pocetno_vrijeme),
            zavrsno_vrijeme = minute_u_hhmm(pravilo.zavrsno_vrijeme),
            naslov = pravilo.naslov
        ) for pravilo in pravila
    ]


@router.put("/tjedno", response_model=List[TjednoPraviloPrikaz])
def spremi_tjedna_pravila(
    body: List[TjednoPravilo],
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db)
):
    opg = opg_ili_404(db, id_korisnika)

    postoji = {p.dan_u_tjednu: p for p in db.query(OpgTjednaRaspolozivost).filter_by(opg_id = opg.id).all()}
    prikaz = []

    for pravilo in body:
        if pravilo.odabrano and hhmm_u_minute(pravilo.pocetno_vrijeme) >= hhmm_u_minute(
            pravilo.zavrsno_vrijeme
        ):
            raise HTTPException(
                status_code=400, detail="Završno vrijeme mora biti veće od početnog"
            )
        redak = postoji.get(pravilo.dan_u_tjednu) or OpgTjednaRaspolozivost(
            opg_id=opg.id, dan_u_tjednu=pravilo.dan_u_tjednu
        )
        redak.odabrano = pravilo.odabrano
        redak.pocetno_vrijeme = hhmm_u_minute(pravilo.pocetno_vrijeme)
        redak.zavrsno_vrijeme = hhmm_u_minute(pravilo.zavrsno_vrijeme)
        redak.naslov = pravilo.naslov
        db.add(redak)
        db.flush()
        prikaz.append(redak)
    
    db.commit()

    return [
        TjednoPraviloPrikaz(
            id = p.id,
            dan_u_tjednu = p.dan_u_tjednu,
            odabrano = p.odabrano,
            pocetno_vrijeme = minute_u_hhmm(p.pocetno_vrijeme),
            zavrsno_vrijeme = minute_u_hhmm(p.zavrsno_vrijeme),
            naslov = p.naslov 
        ) for p in prikaz
    ]


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
    
    dan = OpgRaspolozivostPoDatumu(opg_id = opg.id, datum = body.datum, pocetno_vrijeme = pocetno_vrijeme, zavrsno_vrijeme = zavrsno_vrijeme, naslov = body.naslov)
    
    db.add(dan)
    db.commit()
    db.refresh(dan)
    
    return DatumRapolozivostiPrikaz(id = dan.id, datum = dan.datum, pocetno_vrijeme = body.pocetno_vrijeme, zavrsno_vrijeme = body.zavrsno_vrijeme, naslov = dan.naslov)

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
    
    tjedno = {d.dan_u_tjednu: d for d in db.query(OpgTjednaRaspolozivost).filter_by(opg_id = opg_id).all()}
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
       
        else:
            t = tjedno.get( (d.weekday() + 6) % 7)
            if t and t.odabrano:
                raspon.append( (minute_u_hhmm(t.pocetno_vrijeme), minute_u_hhmm(t.zavrsno_vrijeme)) )
        
        if raspon:
            slotovi[key] = raspon
        
        d += timedelta(days=1)

    return MjeseciKalendaraPrikaz(slotovi=slotovi)

