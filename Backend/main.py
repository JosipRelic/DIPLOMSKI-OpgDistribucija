from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routers import autentifikacija, korisnicki_profil, uredi_ponudu_etrznica, uredi_ponudu_farmaplus, etrznica, farma_plus, opg_raspolozivost, kosarica, narudzbe, opg_primljene_narudzbe, opg_napravljene_narudzbe, opg_nadzorna_ploca, kupac_moje_narudzbe, kupac_nadzorna_ploca, pocetna, ai
from starlette.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from admin import mount_admin
import os
from seeds import seed_kategorije_proizvoda, seed_kategorije_usluga
from database import SessionLocal
from contextlib import asynccontextmanager

API_PREFIX = "/api"


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

app.add_middleware(SessionMiddleware, session_cookie="admin_session", same_site="lax", secret_key=os.getenv("ADMIN_SESSION_SECRET"))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(autentifikacija.router, prefix=API_PREFIX)
app.include_router(korisnicki_profil.router, prefix=API_PREFIX)
app.include_router(uredi_ponudu_etrznica.router, prefix=API_PREFIX)
app.include_router(uredi_ponudu_farmaplus.router, prefix=API_PREFIX)
app.include_router(etrznica.router, prefix=API_PREFIX)
app.include_router(farma_plus.router, prefix=API_PREFIX)
app.include_router(opg_raspolozivost.router, prefix=API_PREFIX)
app.include_router(kosarica.router, prefix=API_PREFIX)
app.include_router(narudzbe.router, prefix=API_PREFIX)
app.include_router(opg_primljene_narudzbe.router, prefix=API_PREFIX)
app.include_router(opg_napravljene_narudzbe.router, prefix=API_PREFIX)
app.include_router(opg_nadzorna_ploca.router, prefix=API_PREFIX)
app.include_router(kupac_moje_narudzbe.router, prefix=API_PREFIX)
app.include_router(kupac_nadzorna_ploca.router, prefix=API_PREFIX)
app.include_router(pocetna.router, prefix=API_PREFIX)
app.include_router(ai.router, prefix=API_PREFIX)

@app.get("/admin", include_in_schema=False)
@app.get("/admin/", include_in_schema=False)
async def admin_pocetna():
    return RedirectResponse(url="/admin/korisnik/list")

mount_admin(app)
