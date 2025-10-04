from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import autentifikacija, korisnicki_profil, uredi_ponudu_etrznica, uredi_ponudu_farmaplus, etrznica, farma_plus, opg_raspolozivost, kosarica, narudzbe, opg_primljene_narudzbe, opg_napravljene_narudzbe, opg_nadzorna_ploca, kupac_moje_narudzbe, kupac_nadzorna_ploca, pocetna
from starlette.staticfiles import StaticFiles
from seeds import seed_kategorije_proizvoda, seed_kategorije_usluga
from database import SessionLocal
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        seed_kategorije_proizvoda(db)
        seed_kategorije_usluga(db)
    finally:
        db.close()

    yield

app = FastAPI(title="OPG Distribucija API", description="API je napravljen u svrhu diplomskog rada", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(autentifikacija.router)
app.include_router(korisnicki_profil.router)
app.include_router(uredi_ponudu_etrznica.router)
app.include_router(uredi_ponudu_farmaplus.router)
app.include_router(etrznica.router)
app.include_router(farma_plus.router)
app.include_router(opg_raspolozivost.router)
app.include_router(kosarica.router)
app.include_router(narudzbe.router)
app.include_router(opg_primljene_narudzbe.router)
app.include_router(opg_napravljene_narudzbe.router)
app.include_router(opg_nadzorna_ploca.router)
app.include_router(kupac_moje_narudzbe.router)
app.include_router(kupac_nadzorna_ploca.router)
app.include_router(pocetna.router)

