from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import autentifikacija

app = FastAPI(title="OPG Distribucija API", description="API je napravljen u svrhu diplomskog rada")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(autentifikacija.router)




