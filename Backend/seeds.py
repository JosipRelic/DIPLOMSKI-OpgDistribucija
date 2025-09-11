from sqlalchemy.orm import Session
from models import KategorijaProizvoda, KategorijaUsluge
from utils import slugify

INICIJALNE_KATEGORIJE_PROIZVODA = [
    "Domaće voće",
    "Sezonsko povrće",
    "Jaja i mliječni proizvodi",
    "Iz košnice",
    "Domaća pića i rakije",
    "Ulja iz prirode",
    "Čajevi i začinsko bilje",
    "Suhomesnati proizvodi",
    "Prirodna kozmetika",
    "Iz šume i dvorišta",
]

INICIJALNE_KATEGORIJE_USLUGA = [
    "Priprema tla",
    "Sjetva i sadnja",
    "Navodnjavanje",
    "Zaštita bilja i gnojidba",
    "Berba i žetva",
    "Skladištenje i prijevoz",
    "Održavanje i dodatne usluge",
    "Prodaja/najam stoke i stočarska pomoć",
]

def seed_kategorije_proizvoda(db:Session):
    for naziv_kategorije in INICIJALNE_KATEGORIJE_PROIZVODA:
        slug = slugify(naziv_kategorije)
        kategorija_postoji = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == slug).first()
        if not kategorija_postoji:
            nova_kategorija = KategorijaProizvoda(naziv=naziv_kategorije, slug=slug)
            db.add(nova_kategorija)

    db.commit()

def seed_kategorije_usluga(db:Session):
    for naziv_kategorije in INICIJALNE_KATEGORIJE_USLUGA:
        slug = slugify(naziv_kategorije)
        kategorija_postoji = db.query(KategorijaUsluge).filter(KategorijaUsluge.slug == slug).first()
        if not kategorija_postoji:
            nova_kategorija = KategorijaUsluge(naziv=naziv_kategorije, slug=slug)
            db.add(nova_kategorija)

    db.commit()