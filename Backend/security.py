from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import Korisnik
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hashiranje_lozinke(lozinka: str) -> str:
    return pwd_context.hash(lozinka)

def verifikacija_lozinke(lozinka_u_tekstualnom_obliku: str, hashirana_lozinka: str) -> bool:
    return pwd_context.verify(lozinka_u_tekstualnom_obliku, hashirana_lozinka)

def kreiranje_tokena_za_pristup(subjekt: str | int, tip_korisnika: str | None = None) -> str:
    trenutno_vrijeme = datetime.now(timezone.utc)
    istice = trenutno_vrijeme + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    trenutno_vrijeme = datetime.now(timezone.utc)
    podaci_za_enkodiranje = {"sub": str(subjekt), "iat": int(trenutno_vrijeme.timestamp()), "exp": int(istice.timestamp())}
    if tip_korisnika:
        podaci_za_enkodiranje["role"] = tip_korisnika
    return jwt.encode(podaci_za_enkodiranje, SECRET_KEY, algorithm=ALGORITHM)

#dekodiranje i provjera jwt tokena, funkcija će vratit payload ili none ako je token neispravan ili istekao
def dekodiraj_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/autentifikacija/prijava")

#funkcija dohvaća trenutno ulogiranog korisnika na temelju jwt tokena
def dohvati_id_trenutnog_korisnika(
        token: str = Depends(oauth2_schema)
) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub = payload.get("sub")
        if not sub:
            raise HTTPException(status_code=401, detail="Neispravan token")
        return int(sub)
    except JWTError:
        raise HTTPException(status_code=401, detail="Neispravan token")

   