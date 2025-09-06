from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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