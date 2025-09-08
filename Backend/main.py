from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import autentifikacija, korisnicki_profil
from starlette.staticfiles import StaticFiles

app = FastAPI(title="OPG Distribucija API", description="API je napravljen u svrhu diplomskog rada")

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




