from sqladmin import Admin, ModelView
from sqlalchemy import event, inspect
from sqlalchemy.orm import Session as SASession
from database import engine
from models import (
    Korisnik, KorisnickiProfil, Kupac, Opg, KategorijaProizvoda, Proizvod,
    KategorijaUsluge, Usluga, Recenzija, OpgRaspolozivostPoDatumu,
    KosaricaStavka, Narudzba, NarudzbaStavka
)
import os
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from dotenv import load_dotenv
from mail import posalji_email_opg_verificiran

load_dotenv()
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")


class AutentifikacijaAdmin(AuthenticationBackend):
    def __init__(self, secret_key: str):
        super().__init__(secret_key=secret_key)

    async def login(self, request: Request) -> bool:
        form = await request.form()
        u = form.get("username")
        p = form.get("password")
        if u == ADMIN_USER and p == ADMIN_PASS:
            request.session.update({"is_admin": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return bool(request.session.get("is_admin"))

@event.listens_for(SASession, "after_flush")
def _posalji_mail_kad_se_opg_verificira(session: SASession, ctx):
    """Nakon flush-a provjeri je li neki OPG upravo postao verificiran i pošalji mail."""
    for inst in session.dirty:
        if isinstance(inst, Opg):
            try:
                hist = inspect(inst).attrs.verificiran.history  
                if hist.has_changes() and bool(inst.verificiran) is True:   
                    email = getattr(getattr(inst, "korisnik", None), "email", None)
                    if email:
                        try:
                            posalji_email_opg_verificiran(email_opg=email, naziv_opg=inst.naziv or "OPG")
                        except Exception as e:
                            print("Greška pri slanju maila OPG-u nakon verifikacije:", e)
            except Exception:
                pass


class KorisnikAdmin(ModelView, model=Korisnik):
    name = "Korisnik"
    name_plural = "Korisnici"
    column_list = [Korisnik.id, Korisnik.ime, Korisnik.prezime, Korisnik.email, Korisnik.korisnicko_ime, Korisnik.tip_korisnika]
    column_searchable_list = [Korisnik.korisnicko_ime, Korisnik.email]
    form_excluded_columns = [
        Korisnik.korisnicki_profil,
        Korisnik.kupac,
        Korisnik.opg,
        Korisnik.recenzije,
    ]

class KorisnickiProfilAdmin(ModelView, model=KorisnickiProfil):
    name = "Korisnički profil"
    name_plural = "Korisnički profili"
    column_list = [KorisnickiProfil.id, KorisnickiProfil.korisnik , KorisnickiProfil.grad, KorisnickiProfil.drzava]
    form_excluded_columns = [
        KorisnickiProfil.korisnik
    ]

class KupacAdmin(ModelView, model=Kupac):
    name = "Kupac"
    name_plural = "Kupci"
    column_list = [Kupac.id, Kupac.korisnik, Kupac.slug, Kupac.datum_pridruzivanja]
    form_excluded_columns =[
        Kupac.korisnik
    ]

class OpgAdmin(ModelView, model=Opg):
    name = "OPG"
    name_plural = "OPG-ovi"
    column_list = [Opg.id, Opg.korisnik, Opg.naziv, Opg.verificiran, Opg.identifikacijski_broj_mibpg, Opg.slug]
    column_searchable_list = [Opg.naziv, Opg.identifikacijski_broj_mibpg]
    form_excluded_columns = [
        Opg.korisnik,
        Opg.proizvodi,
        Opg.usluge,
        Opg.raspolozivost_po_datumu,
        Opg.recenzije,
        Opg.prosjecna_ocjena,
        Opg.broj_recenzija,
    ]

class KategorijaProizvodaAdmin(ModelView, model=KategorijaProizvoda):
    name = "Kategorija proizvoda"
    name_plural = "Kategorije proizvoda"
    column_list = [KategorijaProizvoda.id, KategorijaProizvoda.naziv, KategorijaProizvoda.slug]
    form_excluded_columns = [
        KategorijaProizvoda.proizvodi,
    ]

class ProizvodAdmin(ModelView, model=Proizvod):
    name = "Proizvod"
    name_plural = "Proizvodi"
    column_list = [Proizvod.id, Proizvod.opg, Proizvod.kategorija, Proizvod.naziv, Proizvod.cijena, Proizvod.proizvod_dostupan, Proizvod.opg_id]
    form_excluded_columns = [
        Proizvod.opg,
        Proizvod.kategorija,
    ]

class KategorijaUslugeAdmin(ModelView, model=KategorijaUsluge):
    name = "Kategorija usluge"
    name_plural = "Kategorije usluga"
    column_list = [KategorijaUsluge.id, KategorijaUsluge.naziv, KategorijaUsluge.slug]
    form_excluded_columns = [
        KategorijaUsluge.usluge
    ]

class UslugaAdmin(ModelView, model=Usluga):
    name = "Usluga"
    name_plural = "Usluge"
    column_list = [Usluga.id, Usluga.opg, Usluga.kategorija, Usluga.naziv, Usluga.cijena, Usluga.usluga_dostupna, Usluga.opg_id]
    form_excluded_columns = [
        Usluga.kategorija,
        Usluga.opg,
    ]

class RecenzijaAdmin(ModelView, model=Recenzija):
    name = "Recenzija"
    name_plural = "Recenzije"
    column_list = [Recenzija.id, Recenzija.opg, Recenzija.korisnik, Recenzija.ocjena, Recenzija.opg_id, Recenzija.korisnik_id]
    form_excluded_columns = [
        Recenzija.opg,
        Recenzija.korisnik,
    ]

class OpgRaspolozivostAdmin(ModelView, model=OpgRaspolozivostPoDatumu):
    name = "Opg raspoloživost"
    name_plural = "Opg-ovi raspoloživost"
    column_list = [OpgRaspolozivostPoDatumu.opg, OpgRaspolozivostPoDatumu.id, OpgRaspolozivostPoDatumu.datum, OpgRaspolozivostPoDatumu.pocetno_vrijeme, OpgRaspolozivostPoDatumu.zavrsno_vrijeme, OpgRaspolozivostPoDatumu.opg_id]
    form_excluded_columns = [
        OpgRaspolozivostPoDatumu.opg
    ]

class KosaricaStavkaAdmin(ModelView, model=KosaricaStavka):
    name = "Košarica stavka"
    name_plural = "Košarica stavke"
    column_list = [KosaricaStavka.id, KosaricaStavka.korisnik_id, KosaricaStavka.proizvod, KosaricaStavka.usluga, KosaricaStavka.termin_od, KosaricaStavka.termin_do, KosaricaStavka.kolicina, KosaricaStavka.cijena]
    form_excluded_columns = [
        KosaricaStavka.proizvod,
        KosaricaStavka.usluga,
        KosaricaStavka.termin_od,
        KosaricaStavka.termin_do,
    ]

class NarudzbaAdmin(ModelView, model=Narudzba):
    name = "Narudžba"
    name_plural = "Narudžbe"
    column_list = [Narudzba.id, Narudzba.ime, Narudzba.prezime, Narudzba.email, Narudzba.telefon, Narudzba.broj_narudzbe, Narudzba.ukupno, Narudzba.korisnik_id, Narudzba.datum_izrade]
    form_excluded_columns = [
        Narudzba.stavke,

    ]

class NarudzbaStavkaAdmin(ModelView, model=NarudzbaStavka):
    name = "Narudžba stavka"
    name_plural = "Narudžba stavke"
    column_list = [NarudzbaStavka.id, NarudzbaStavka.narudzba, NarudzbaStavka.tip, NarudzbaStavka.naziv, NarudzbaStavka.mjerna_jedinica, NarudzbaStavka.kolicina, NarudzbaStavka.cijena, NarudzbaStavka.status, NarudzbaStavka.opg_id]
    form_excluded_columns = [
        NarudzbaStavka.narudzba
    ]


def mount_admin(app):
    secret = os.getenv("ADMIN_SESSION_SECRET")
   
    admin = Admin(app, engine, title="OPG Distribucija - Admin", authentication_backend=AutentifikacijaAdmin(secret_key=secret))
    admin.add_view(KorisnikAdmin)
    admin.add_view(KorisnickiProfilAdmin)
    admin.add_view(KupacAdmin)
    admin.add_view(OpgAdmin)
    admin.add_view(KategorijaProizvodaAdmin)
    admin.add_view(ProizvodAdmin)
    admin.add_view(KategorijaUslugeAdmin)
    admin.add_view(UslugaAdmin)
    admin.add_view(RecenzijaAdmin)
    admin.add_view(OpgRaspolozivostAdmin)
    admin.add_view(KosaricaStavkaAdmin)
    admin.add_view(NarudzbaAdmin)
    admin.add_view(NarudzbaStavkaAdmin)
    return admin