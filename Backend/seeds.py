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

INICIJALNE_KATEGORIJE_PROIZVODA_META = {
    "domace-voce": {
        "opis": "Uživajte u bogatstvu okusa i mirisa domaćeg voća uzgojenog s pažnjom i ljubavlju na hrvatskim OPG-ovima.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-voce.jpg"
    },
    "sezonsko-povrce": {
        "opis": "Povrće ubrano u svom prirodnom ritmu. Lokalne sorte, bogatog okusa i nutritivne vrijednosti savršeno za zdravu i uravnoteženu prehranu.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-povrce.jpg"
    },
    "jaja-i-mlijecni-proizvodi": {
        "opis": "Domaća jaja, sir, vrhnje i drugi mliječni proizvodi s farmi koje njeguju tradicionalnu proizvodnju bez industrijskih dodataka.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-mlijecniproizvodi.jpg"
    },
    "iz-kosnice": {
        "opis": "Prirodni pčelinji proizvodi poput meda, propolisa i voska. Prikupljeni s netaknutih livada i šuma, idealni za jačanje imuniteta i svakodnevnu upotrebu.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-izkosnice.jpg"
    },
    "domaca-pica-i-rakije": {
        "opis": "Autentične domaće rakije, likeri i voćna vina. Ručno rađeni recepti i domaće voće stvaraju pića koja pričaju priču svog kraja.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-pica.jpg"
    },
    "ulja-iz-prirode": {
        "opis": "Hladno prešana ulja od buče, suncokreta, masline i drugih biljaka. Bogata hranjivim tvarima, odlična za kuhanje, salate i njegu tijela.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-ulja.jpg"
    },
    "cajevi-i-zacinsko-bilje": {
        "opis": "Ručno ubrano ljekovito bilje i začini iz ekološkog uzgoja. Začini puni arome i čajevi koji opuštaju i obnavljaju duh i tijelo.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-cajevi-zacini.jpg"
    },
    "suhomesnati-proizvodi": {
        "opis": "Tradicionalno sušene kobasice, pancete i čvarci. Bez aditiva i konzervansa, napravljeni prema receptima koji se prenose generacijama.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-suhomesnato.jpg"
    },
    "prirodna-kozmetika": {
        "opis": "Balzami, kreme, sapuni i ulja na bazi prirodnih sastojaka. Ručno rađeni proizvodi za njegu kože bez štetnih kemikalija.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-kozmetika.jpg"
    },
    "iz-sume-i-dvorista": {
        "opis": "Divlje gljive, orašasti plodovi i plodovi iz dvorišta kesteni, lješnjaci, orasi i drugo bogatstvo domaće prirode.",
        "slika_kategorije": "/static/assets/etrznica-kategorije-sumaidvoriste.jpg"
    }
}

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
        kategorija = db.query(KategorijaProizvoda).filter(KategorijaProizvoda.slug == slug).first()
        if not kategorija:
            meta = INICIJALNE_KATEGORIJE_PROIZVODA_META.get(slug, {})
            db.add(KategorijaProizvoda(naziv=naziv_kategorije, slug=slug, opis=meta.get("opis"), slika_kategorije=meta.get("slika_kategorije")))
        else:
            meta = INICIJALNE_KATEGORIJE_PROIZVODA_META.get(slug, {})
            if not kategorija.opis and meta.get("opis"):
                kategorija.opis = meta["opis"]
            if not kategorija.slika_kategorije and meta.get("slika_kategorije"):
                kategorija.slika_kategorije = meta["slika_kategorije"]

    db.commit()

def seed_kategorije_usluga(db:Session):
    for naziv_kategorije in INICIJALNE_KATEGORIJE_USLUGA:
        slug = slugify(naziv_kategorije)
        kategorija_postoji = db.query(KategorijaUsluge).filter(KategorijaUsluge.slug == slug).first()
        if not kategorija_postoji:
            nova_kategorija = KategorijaUsluge(naziv=naziv_kategorije, slug=slug)
            db.add(nova_kategorija)

    db.commit()