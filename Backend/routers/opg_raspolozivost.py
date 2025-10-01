from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import Date, cast, func
from typing import List, Dict, Optional
from datetime import date, datetime, timedelta
from models import Korisnik, Kupac, Opg, OpgRaspolozivostPoDatumu, NarudzbaStavka, Narudzba, Usluga
from schemas import  DatumRaspolozivosti, DatumRapolozivostiPrikaz, MjeseciKalendaraPrikaz, RasponKalendaraPrikaz
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
    
    danas = date.today()
    if body.datum < danas:
        raise HTTPException(status_code=400, detail="Datum je u prošlosti") 

    if body.datum == danas:
        now = datetime.now()
        now_min = now.hour * 60 + now.minute
        if pocetak < now_min:
            raise HTTPException(status_code=400, detail="Početno vrijeme je u prošlosti")
        if zavrsetak <= now_min:
            raise HTTPException(status_code=400, detail="Završno vrijeme je u prošlosti")


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

    dani_po_datumu: Dict[date, list[tuple[int, int, Optional[str]]]] = {}

    for dan in dnevno:
        dani_po_datumu.setdefault(dan.datum, []).append((dan.pocetno_vrijeme, dan.zavrsno_vrijeme, dan.naslov))

    slotovi: Dict[str, list[RasponKalendaraPrikaz]] = {}
    d = pocetak

    while d <= kraj:
        key = d.isoformat()
        raspon: List[RasponKalendaraPrikaz] = []

        if d in dani_po_datumu:
            for p, k, n in sorted(dani_po_datumu[d]):
                raspon.append( RasponKalendaraPrikaz(
                    od = minute_u_hhmm(p),
                    do = minute_u_hhmm(k),
                    naslov = n,
                ))
        
        if raspon:
            slotovi[key] = raspon
        
        d += timedelta(days=1)

    return MjeseciKalendaraPrikaz(slotovi=slotovi)


def _oduzmi_rezervaciju_od_raspolozivosti(db: Session, opg_id: int, d: date, pocetno_vrijeme: int, zavrsno_vrijeme: int):

    if pocetno_vrijeme >= zavrsno_vrijeme:
        return
    
    termini = (
        db.query(OpgRaspolozivostPoDatumu)
        .filter(
            OpgRaspolozivostPoDatumu.opg_id == opg_id,
            OpgRaspolozivostPoDatumu.datum == d,
            OpgRaspolozivostPoDatumu.pocetno_vrijeme < zavrsno_vrijeme,
            OpgRaspolozivostPoDatumu.zavrsno_vrijeme > pocetno_vrijeme,
        )
        .order_by(OpgRaspolozivostPoDatumu.pocetno_vrijeme.asc())
        .all()
    )

    for t in termini:
        p = t.pocetno_vrijeme
        z = t.zavrsno_vrijeme

        if zavrsno_vrijeme <= p or pocetno_vrijeme >= z:
            continue

        if pocetno_vrijeme <= p and zavrsno_vrijeme >= z:
            db.delete(t)
            continue

        if pocetno_vrijeme > p and zavrsno_vrijeme < z:
            lijevi_raspon = OpgRaspolozivostPoDatumu(
                opg_id = opg_id, datum = d, pocetno_vrijeme = p, zavrsno_vrijeme = pocetno_vrijeme, naslov = t.naslov
            )
            desni_raspon = OpgRaspolozivostPoDatumu(
                opg_id = opg_id, datum = d, pocetno_vrijeme = zavrsno_vrijeme, zavrsno_vrijeme = z, naslov = t.naslov
            )
            
            db.delete(t)
            db.add(lijevi_raspon)
            db.add(desni_raspon)
            continue
        
        if pocetno_vrijeme <= p < zavrsno_vrijeme < z:
            t.pocetno_vrijeme = zavrsno_vrijeme
            continue

        if p < pocetno_vrijeme < z <= zavrsno_vrijeme:
            t.zavrsno_vrijeme = pocetno_vrijeme
            continue


def _opg_id_iz_korisnika(db: Session, korisnik_id: int) -> int:
    opg = db.query(Opg).filter(Opg.korisnik_id == korisnik_id).first()
    if not opg:
        raise HTTPException(status_code=404, detail="OPG nije pronađen")
    return opg.id

@router.get("/po-danu")
def rezervacije_po_danu(
    opg_id: int = Query(..., ge=1),
    godina: int = Query(..., ge=2000, le=2100),
    mjesec: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db),
):
   
    start = date(godina, mjesec, 1)
    if mjesec == 12:
        end = date(godina + 1, 1, 1)
    else:
        end = date(godina, mjesec + 1, 1)

    rezervacije = (
        db.query(func.date(NarudzbaStavka.termin_od).label("d"), func.count())
        .join(Usluga, Usluga.id == NarudzbaStavka.usluga_id)
        .filter(
            NarudzbaStavka.tip == "usluga",
            NarudzbaStavka.termin_od.isnot(None),
            NarudzbaStavka.termin_od >= start,
            NarudzbaStavka.termin_od <  end,
            Usluga.opg_id == opg_id,
        )
        .group_by("d")
        .order_by("d")
    )

    datumi = {}
    for d, cnt in rezervacije.all():
        datumi[d.isoformat()] = int(cnt)
    

    return {"datumi": datumi}


@router.get("")
def sve_rezervacije(
    limit: int = Query(0, ge=0, le=200),
    id_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    db: Session = Depends(get_db),
):
    opg_id = _opg_id_iz_korisnika(db, id_korisnika)

    termini_stavke_narudzbe = (
        db.query(
            Usluga.slika_usluge.label("slika"),
            NarudzbaStavka.naziv.label("usluga"),
            NarudzbaStavka.kolicina,
            NarudzbaStavka.mjerna_jedinica,
            NarudzbaStavka.termin_od,
            NarudzbaStavka.termin_do,
            Narudzba.broj_narudzbe,
            Narudzba.ime,
            Narudzba.id.label("narudzba_id"),
            Narudzba.prezime,
            Korisnik.tip_korisnika.label("narucitelj_tip"),
            Kupac.slug.label("kupac_slug"),
            Opg.slug.label("opg_slug"),       
        )
        .join(Narudzba, NarudzbaStavka.narudzba_id == Narudzba.id)
        .join(Usluga, Usluga.id == NarudzbaStavka.usluga_id)
        .join(Korisnik, Korisnik.id == Narudzba.korisnik_id)
        .outerjoin(Kupac, Kupac.korisnik_id == Korisnik.id)
        .outerjoin(Opg, Opg.korisnik_id == Korisnik.id)
        .filter(
            NarudzbaStavka.tip == "usluga",
            NarudzbaStavka.termin_od != None,
            Usluga.opg_id == opg_id,
            NarudzbaStavka.termin_do >= datetime.now()
        )
        .order_by(NarudzbaStavka.termin_od.asc())
    )

    if limit > 0:
        termini_stavke_narudzbe = termini_stavke_narudzbe.limit(limit)
    
    termini = [
        {
            "usluga": termin.usluga,
            "slika": termin.slika,
            "kolicina": termin.kolicina,
            "mjerna_jedinica": termin.mjerna_jedinica,
            "termin_od": termin.termin_od.isoformat(),
            "termin_do": termin.termin_do.isoformat(),
            "broj_narudzbe": termin.broj_narudzbe,
            "narudzba_id": termin.narudzba_id,
            "kupac": f"{termin.ime} {termin.prezime}",
            "narucitelj_tip": termin.narucitelj_tip, 
            "kupac_slug": termin.kupac_slug,          
            "opg_slug": termin.opg_slug,
        } for termin in termini_stavke_narudzbe.all()
    ]

    return {"termini": termini}