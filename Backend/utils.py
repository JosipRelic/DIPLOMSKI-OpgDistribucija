import re, unicodedata

def slugify(tekst: str) -> str:
    tekst = unicodedata.normalize("NFKD", tekst).encode("ascii", "ignore").decode("utf-8")
    tekst = re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")
    return tekst or "korisnik"