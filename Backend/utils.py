import re, unicodedata
from pathlib import Path
from urllib.parse import urlparse

def slugify(tekst: str) -> str:
    tekst = unicodedata.normalize("NFKD", tekst).encode("ascii", "ignore").decode("utf-8")
    tekst = re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")
    return tekst or "korisnik"

BAZNI_DIREKTORIJ = Path(__file__).resolve().parent
STATIC_RUTA = "/static/uploads/"

def obrisi_uploadanu_sliku(url_slike: str) -> None:
    try:
        path = urlparse(url_slike).path
        if not path.startswith(STATIC_RUTA):
            return
        fs_path = BAZNI_DIREKTORIJ / path.lstrip("/")
        if fs_path.exists():
            fs_path.unlink()
    except Exception:
        pass
