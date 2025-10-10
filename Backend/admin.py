from sqladmin import Admin, ModelView
from sqlalchemy import event, inspect
from sqlalchemy.orm import Session as SASession
from database import engine
from models import (
    Korisnik, KorisnickiProfil, Kupac, Opg, KategorijaProizvoda, Proizvod,
    KategorijaUsluge, Usluga, Recenzija, OpgRaspolozivostPoDatumu,
    KosaricaStavka, Narudzba, NarudzbaStavka
)
from mail import posalji_email_opg_verificiran

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
    column_list = [Korisnik.id, Korisnik.email, Korisnik.korisnicko_ime, Korisnik.tip_korisnika]

class KorisnickiProfilAdmin(ModelView, model=KorisnickiProfil):
    name = "Korisnički profil"
    name_plural = "Korisnički profili"
    column_list = [KorisnickiProfil.id, KorisnickiProfil.grad, KorisnickiProfil.drzava]

class KupacAdmin(ModelView, model=Kupac):
    name = "Kupac"
    name_plural = "Kupci"
    column_list = [Kupac.id, Kupac.slug, Kupac.datum_pridruzivanja]

class OpgAdmin(ModelView, model=Opg):
    name = "OPG"
    name_plural = "OPG-ovi"
    column_list = [Opg.id, Opg.naziv, Opg.verificiran, Opg.identifikacijski_broj_mibpg, Opg.slug]

class KategorijaProizvodaAdmin(ModelView, model=KategorijaProizvoda):
    name = "Kategorija proizvoda"
    name_plural = "Kategorije proizvoda"
    column_list = [KategorijaProizvoda.id, KategorijaProizvoda.naziv, KategorijaProizvoda.slug]

class ProizvodAdmin(ModelView, model=Proizvod):
    name = "Proizvod"
    name_plural = "Proizvodi"
    column_list = [Proizvod.id, Proizvod.naziv, Proizvod.cijena, Proizvod.proizvod_dostupan, Proizvod.opg_id]

class KategorijaUslugeAdmin(ModelView, model=KategorijaUsluge):
    name = "Kategorija usluge"
    name_plural = "Kategorije usluga"
    column_list = [KategorijaUsluge.id, KategorijaUsluge.naziv, KategorijaUsluge.slug]

class UslugaAdmin(ModelView, model=Usluga):
    name = "Usluga"
    name_plural = "Usluge"
    column_list = [Usluga.id, Usluga.naziv, Usluga.cijena, Usluga.usluga_dostupna, Usluga.opg_id]

class RecenzijaAdmin(ModelView, model=Recenzija):
    name = "Recenzija"
    name_plural = "Recenzije"
    column_list = [Recenzija.id, Recenzija.ocjena, Recenzija.opg_id, Recenzija.korisnik_id]

class OpgRaspolozivostAdmin(ModelView, model=OpgRaspolozivostPoDatumu):
    name = "Opg raspoloživost"
    name_plural = "Opg-ovi raspoloživost"
    column_list = [OpgRaspolozivostPoDatumu.id, OpgRaspolozivostPoDatumu.datum, OpgRaspolozivostPoDatumu.opg_id]

class KosaricaStavkaAdmin(ModelView, model=KosaricaStavka):
    name = "Košarica stavka"
    name_plural = "Košarica stavke"
    column_list = [KosaricaStavka.id, KosaricaStavka.kolicina, KosaricaStavka.cijena, KosaricaStavka.korisnik_id]

class NarudzbaAdmin(ModelView, model=Narudzba):
    name = "Narudžba"
    name_plural = "Narudžbe"
    column_list = [Narudzba.id, Narudzba.broj_narudzbe, Narudzba.ukupno, Narudzba.korisnik_id, Narudzba.datum_izrade]

class NarudzbaStavkaAdmin(ModelView, model=NarudzbaStavka):
    name = "Narudžba stavka"
    name_plural = "Narudžba stavke"
    column_list = [NarudzbaStavka.id, NarudzbaStavka.tip, NarudzbaStavka.naziv, NarudzbaStavka.status, NarudzbaStavka.opg_id]


def mount_admin(app):
    admin = Admin(app, engine, title="OPG Distribucija - Admin")
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