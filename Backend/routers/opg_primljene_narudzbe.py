import math
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from database import SessionLocal
from sqlalchemy import desc, func, or_
from security import dohvati_id_trenutnog_korisnika
from models import Korisnik, Kupac, Opg, Narudzba, NarudzbaStavka, Proizvod, TipKorisnika, Usluga
from schemas import PromjenaStatusaNarudzbe

router = APIRouter(prefix="/opg/primljene-narudzbe", tags=["OPG profil - Primljene narudžbe"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _moj_opg_id (db: Session, korisnik_id: int) -> int:
    k = db.get(Korisnik, korisnik_id)
    if not k or not k.opg:
        raise HTTPException(403, "Niste OPG korisnik")
    return k.opg.id


@router.get("")
def primljene_narudzbe(
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    stranica: int = Query(1, ge=1),
    velicina: int = Query(8, ge=1, le=100),
    p: str | None = Query(None)
):
    opg_id = _moj_opg_id(db, id_trenutnog_korisnika)

    narudzba = (
        db.query(Narudzba.id, Narudzba.broj_narudzbe, Narudzba.ukupno, Narudzba.datum_izrade, Narudzba.ime, Narudzba.prezime)
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .filter(NarudzbaStavka.opg_id == opg_id)
    )

    if p:
        like = f"%{p.strip()}%"
        narudzba = narudzba.filter(Narudzba.broj_narudzbe.ilike(like))
    
    pod_idevi = narudzba.with_entities(Narudzba.id).distinct().subquery()
    ukupno = db.query(func.count()).select_from(pod_idevi).scalar() or 0

    id_stranice = (
        db.query(pod_idevi.c.id)
        .offset((stranica-1) * velicina)
        .limit(velicina)
        .all()
    )

    idevi = [i[0] for i in id_stranice]

    if not idevi:
        return {"narudzbe": [], "ukupno": 0, "ukupno_stranica": 0}
    
    kupci = (
        db.query(
        Narudzba.id.label("nid"),
        Korisnik.tip_korisnika.label("tip"),
        Kupac.slug.label("kupac_slug"),
        Opg.slug.label("opg_slug"),
        )
        .join(Korisnik, Korisnik.id == Narudzba.korisnik_id)
        .outerjoin(Kupac, Kupac.korisnik_id == Korisnik.id)
        .outerjoin(Opg, Opg.korisnik_id == Korisnik.id)  
        .filter(Narudzba.id.in_(idevi))
        .all()
    )

    kupci_po_idu = {
        k.nid: dict(
            tip=k.tip, kupac_slug=k.kupac_slug, opg_slug=k.opg_slug
        ) for k in kupci
    }

    rezultat = []

    for nid in idevi:
        n = db.get(Narudzba, nid)
        
        opg_ukupno = db.query(func.coalesce(func.sum(NarudzbaStavka.kolicina * NarudzbaStavka.cijena), 0.0)) \
                    .filter(NarudzbaStavka.narudzba_id == nid, NarudzbaStavka.opg_id == opg_id).scalar() or 0.0
        
        stavke = (
            db.query(NarudzbaStavka.status)
            .filter(NarudzbaStavka.narudzba_id == nid, NarudzbaStavka.opg_id == opg_id)
            .all()
        )

        s_set = {s[0] for s in stavke}
        if "otkazano" in s_set:
            status = "otkazano"
        elif s_set == {"isporuceno"}:
            status = "isporuceno"
        else:
            status = "u_tijeku"

        if n.nacin_dostave == "dostava":
            opg_ukupno += 5

        kid = kupci_po_idu.get(nid, {})
        rezultat.append(dict(
            id = n.id,
            broj_narudzbe = n.broj_narudzbe,
            ukupno = float(opg_ukupno),
            datum_izrade = n.datum_izrade.isoformat() if n.datum_izrade else None,
            narucitelj = f"{n.ime} {n.prezime}".strip(),
            status = status,
            kupac_slug = kid.get("kupac_slug"),
            opg_slug = kid.get("opg_slug"),
            narucitelj_tip = kid.get("tip"),
        ))
  

    ukupno_stranica = math.ceil((ukupno or 0) / velicina)
    return {"narudzbe": rezultat, "ukupno": ukupno, "ukupno_stranica": ukupno_stranica}


@router.get("/detalji-narudzbe/{narudzba_id}")
def detalji_narudzbe(
    narudzba_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
):
    opg_id = _moj_opg_id(db, id_trenutnog_korisnika)
    n = db.get(Narudzba, narudzba_id)
    if not n:
        raise HTTPException(404, "Narudžba ne postoji")
    
    stavke = (
        db.query(NarudzbaStavka)
        .filter(NarudzbaStavka.narudzba_id == narudzba_id, NarudzbaStavka.opg_id == opg_id)
        .all()
    )

    proizvodi = []
    usluge = []

    for s in stavke:
        stavka = dict(
            id = s.id,
            tip = s.tip,
            naziv = s.naziv,
            kolicina = s.kolicina,
            mjerna_jedinica = s.mjerna_jedinica,
            cijena = float(s.cijena or 0),
            slika = s.slika,
            termin_od = s.termin_od.isoformat() if s.termin_od else None,
            termin_do = s.termin_do.isoformat() if s.termin_do else None,
            status = s.status,
            proizvod_id = s.proizvod_id, 
            usluga_id = s.usluga_id,
        )
        (usluge if s.tip == "usluga" else proizvodi).append(stavka)
    
    s_set = {s["status"] for s in (proizvodi + usluge)}

    if "otkazano" in s_set:
        status = "otkazano"
    elif s_set and s_set == {"isporuceno"}:
        status = "isporuceno"
    else:
        status = "u_tijeku"

    def _bruto(st): return float(st["cijena"] or 0) * float(st["kolicina"] or 0)
    def _neto(st): return _bruto(st)/1.25

    iznos_bez_pdva = round(sum(_neto(s) for s in (proizvodi + usluge)), 2)
    pdv = round(iznos_bez_pdva * 0.25, 2)
    ukupno = round(sum(_bruto(s) for s in (proizvodi + usluge)), 2)

    dostava_po_opgu = 5

    if n.dostava != 0: 
        ukupno = ukupno + dostava_po_opgu
        
    if n.dostava == 0:
        dostava_po_opgu = 0
   
    
    return {
        "id": n.id,
        "broj_narudzbe": n.broj_narudzbe,
        "datum_izrade": n.datum_izrade.isoformat() if n.datum_izrade else None,
        "iznos_bez_pdva": iznos_bez_pdva,
        "pdv": pdv,
        "dostava": float(dostava_po_opgu or 0),
        "ukupno": ukupno,
        "narucitelj": f"{n.ime} {n.prezime}".strip(),
        "kupac_email": n.email,
        "kupac_telefon": n.telefon,
        "adresa": f"{n.adresa}, {n.grad} {n.postanski_broj}",
        "zupanija": n.zupanija,
        "nacin_placanja": n.nacin_placanja,
        "nacin_dostave": n.nacin_dostave,
        "status": status,
        "proizvodi": proizvodi,
        "usluge": usluge,
    }


@router.patch("/detalji-narudzbe/{narudzba_id}/status")
def promijeni_status_narudzbe(
    narudzba_id: int,
    body: PromjenaStatusaNarudzbe,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika)
):
    opg_id = _moj_opg_id(db, id_trenutnog_korisnika)

    narudzba = (
        db.query(NarudzbaStavka)
        .filter(NarudzbaStavka.narudzba_id == narudzba_id, NarudzbaStavka.opg_id == opg_id)
    )

    if not db.query(narudzba.exists()).scalar():
        raise HTTPException(404, "Nije pronađena narudžba za vaš OPG")
    
    narudzba.update({NarudzbaStavka.status: body.status}, synchronize_session=False)
    db.commit()
    return {"status": body.status}



@router.get("/detalji-kupca/{kupac_slug}")
def detalji_kupca(
    kupac_slug: str,
    db: Session = Depends(get_db),
    id_trenutnog_korisnika: int = Depends(dohvati_id_trenutnog_korisnika),
    stranica: int = Query(1, ge=1),
    velicina: int = Query(8, ge=1, le=50),
    p: str | None = Query(None, description="pretraga po broju narudžbe")
):
    
    korisnik = db.get(Korisnik, id_trenutnog_korisnika)
    if not korisnik or korisnik.tip_korisnika != TipKorisnika.opg:
        raise HTTPException(status_code=403, detail="Samo OPG može pristupiti detaljima kupca.")
    
    opg = korisnik.opg
    if not opg:
        raise HTTPException(status_code=404, detail="Opg nije pronađen")
    
    kupac = db.query(Kupac).filter(Kupac.slug == kupac_slug).first()
    if not kupac:
        raise HTTPException(status_code=404, detail="Kupac nije pronađen.")
    
    korisnik_kupac = kupac.korisnik

    narudzbe = (
        db.query(Narudzba)
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .outerjoin(Proizvod, Proizvod.id == NarudzbaStavka.proizvod_id)
        .outerjoin(Usluga, Usluga.id == NarudzbaStavka.usluga_id)
        .filter(
            Narudzba.korisnik_id == korisnik_kupac.id,
            NarudzbaStavka.opg_id == opg.id,
        ).distinct()
    )


    if p:
        like = f"%{p.strip()}%"
        narudzbe = narudzbe.filter(Narudzba.broj_narudzbe.ilike(like))

    
    ukupno = narudzbe.count()

    narudzbe_prikaz = (
        narudzbe
        .order_by(desc(Narudzba.datum_izrade))
        .offset((stranica - 1 ) * velicina)
        .limit(velicina)
        .all()
    )

    narudzbe_idevi_subq = (
        db.query(Narudzba.id)
        .join(NarudzbaStavka, NarudzbaStavka.narudzba_id == Narudzba.id)
        .outerjoin(Proizvod, Proizvod.id == NarudzbaStavka.proizvod_id)
        .outerjoin(Usluga, Usluga.id == NarudzbaStavka.usluga_id)
        .filter(
            Narudzba.korisnik_id == korisnik_kupac.id,
            NarudzbaStavka.opg_id == opg.id,
        )
        .distinct()
        .subquery()
    )

    broj_proizvoda = (
        db.query(func.coalesce(func.sum(NarudzbaStavka.kolicina), 0))
        .filter(
            NarudzbaStavka.narudzba_id.in_(db.query(narudzbe_idevi_subq.c.id)),
            NarudzbaStavka.opg_id == opg.id,           
            NarudzbaStavka.tip == "proizvod",
        )
        .scalar()
    ) or 0

    broj_usluga = (
        db.query(func.coalesce(func.sum(NarudzbaStavka.kolicina), 0))
        .filter(
            NarudzbaStavka.narudzba_id.in_(db.query(narudzbe_idevi_subq.c.id)),
            NarudzbaStavka.opg_id == opg.id,           
            NarudzbaStavka.tip == "usluga",
        )
        .scalar()
    ) or 0

    zadnja_narudzba = (
        db.query(func.max(Narudzba.datum_izrade))
        .filter(Narudzba.id.in_(db.query(narudzbe_idevi_subq.c.id))).scalar()
    )

    ukupna_vrijednost = (
        db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
        .filter(
            NarudzbaStavka.narudzba_id.in_(db.query(narudzbe_idevi_subq.c.id)),
            NarudzbaStavka.opg_id == opg.id,         
        )
        .scalar()
    ) or 0.0

    broj_dostava = (
        db.query(func.count())
        .select_from(Narudzba)
        .filter(
            Narudzba.id.in_(db.query(narudzbe_idevi_subq.c.id)),
            Narudzba.nacin_dostave == "dostava",
        )
        .scalar()
    ) or 0

    ukupna_vrijednost += broj_dostava * 5

    najcesce = (
        db.query(
            NarudzbaStavka.naziv,
            func.coalesce(func.sum(NarudzbaStavka.kolicina), 0).label("zbroj")
        )
        .filter(
            NarudzbaStavka.narudzba_id.in_(db.query(narudzbe_idevi_subq.c.id)),
            NarudzbaStavka.opg_id == opg.id,          
            NarudzbaStavka.tip == "proizvod"         
        )
        .group_by(NarudzbaStavka.naziv)
        .order_by(desc("zbroj"))
        .first()
    )



    najcesce_kupljeno = najcesce[0] if najcesce else None

    narudzbe_izlaz = []
    for n in narudzbe_prikaz:

        opg_ukupno = (
            db.query(func.coalesce(func.sum(NarudzbaStavka.cijena * NarudzbaStavka.kolicina), 0.0))
            .filter(
                NarudzbaStavka.narudzba_id == n.id,
                NarudzbaStavka.opg_id == opg.id,       
            )
            .scalar()
        ) or 0.0

        if n.nacin_dostave == "dostava":
            opg_ukupno += 5

        s_set = {
            s[0] for s in db.query(NarudzbaStavka.status)
            .filter(
                NarudzbaStavka.narudzba_id == n.id,
                NarudzbaStavka.opg_id == opg.id
            ).all()
        }
        if "otkazano" in s_set:
            status = "otkazano"
        elif s_set and s_set == {"isporuceno"}:
            status = "isporuceno"
        else:
            status = "u_tijeku"

        narudzbe_izlaz.append(dict(
            broj_narudzbe = n.broj_narudzbe,
            ukupno = float(opg_ukupno),
            datum_izrade = n.datum_izrade.isoformat() if n.datum_izrade else None,
            status = status,   
            id = n.id,
    ))

    korisnicki_profil_kupca = korisnik_kupac.korisnicki_profil
    kupac_profil = dict(
        ime = korisnik_kupac.ime,
        prezime = korisnik_kupac.prezime,
        email = korisnik_kupac.email,
        broj_telefona = korisnik_kupac.broj_telefona,
        adresa = korisnicki_profil_kupca.adresa if korisnicki_profil_kupca else None,
        grad = korisnicki_profil_kupca.grad if korisnicki_profil_kupca else None,
        postanski_broj = korisnicki_profil_kupca.postanski_broj if korisnicki_profil_kupca else None,
        zupanija = korisnicki_profil_kupca.zupanija if korisnicki_profil_kupca else None,
        slika_profila = korisnicki_profil_kupca.slika_profila if korisnicki_profil_kupca else None,
        slug = kupac.slug
    )

    return {
        "kupac": kupac_profil,
        "statistika": {
            "broj_proizvoda": int(broj_proizvoda or 0),
            "broj_usluga": int(broj_usluga or 0),
            "zadnja_narudzba": zadnja_narudzba.isoformat() if zadnja_narudzba else None,
            "najcesce_kupljeno": najcesce_kupljeno,
            "ukupna_vrijednost": float(ukupna_vrijednost or 0),
        },
        "narudzbe": {
            "ukupno": ukupno,
            "stranica": stranica,
            "velicina": velicina,
            "stavke": narudzbe_izlaz,
        }
    }
