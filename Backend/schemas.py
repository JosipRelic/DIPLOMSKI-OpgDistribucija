from pydantic import BaseModel, Field, EmailStr
from decimal import Decimal
from typing import Literal, Optional
from datetime import datetime, date


class RegistracijaKupac(BaseModel):
    email: EmailStr
    korisnicko_ime: str = Field(min_length=3, max_length=50)
    lozinka: str = Field(min_length=8, max_length=255)
    potvrda_lozinke: str = Field(min_length=8, max_length=255)
    ime: str = Field(min_length=1, max_length=100)
    prezime: str = Field(min_length=1, max_length=100)

class RegistracijaOpg(BaseModel):
    email: EmailStr
    korisnicko_ime: str = Field(min_length=3, max_length=50)
    lozinka: str = Field(min_length=8, max_length=255)
    potvrda_lozinke: str = Field(min_length=8, max_length=255)
    ime: str = Field(min_length=1, max_length=100)
    prezime: str = Field(min_length=1, max_length=100)
    naziv: str = Field(min_length=2, max_length=150)
    opis: Optional[str] = Field(None, max_length=500)
    identifikacijski_broj_mibpg: str = Field(min_length=3, max_length=50)

class Prijava(BaseModel):
    email_ili_korisnicko_ime: str
    lozinka: str


class PrikazKorisnickogProfila(BaseModel):
    id: int
    email: EmailStr
    ime: str = Field(min_length=1, max_length=100)
    prezime: str = Field(min_length=1, max_length=100)
    tip_korisnika: Literal["Kupac", "Opg"]
    broj_telefona: Optional[str] = Field(default=None)
    slika_profila: Optional[str] = Field(default=None)
    drzava: Optional[str] = Field(default=None)
    zupanija: Optional[str] = Field(default=None)
    grad: Optional[str] = Field(default=None)
    postanski_broj: Optional[str] = Field(default=None)
    adresa: Optional[str] = Field(default=None)
    slug: Optional[str] = Field(default=None)

    naziv: Optional[str] = Field(default=None)
    opis: Optional[str] = Field(default=None)
    identifikacijski_broj_mibpg: Optional[str] = Field(default=None)
    
    model_config = {
        "from_attributes": True
    }

class AzuriranjeKorisnickogProfila(BaseModel):
    email: Optional[EmailStr] = Field(default=None)
    ime: Optional[str] = Field(default=None)
    prezime: Optional[str] = Field(default=None)
    broj_telefona: Optional[str] = Field(default=None)
    drzava: Optional[str] = Field(default=None)
    zupanija: Optional[str] = Field(default=None)
    grad: Optional[str] = Field(default=None)
    postanski_broj: Optional[str] = Field(default=None)
    adresa: Optional[str] = Field(default=None)

    slug: Optional[str] = Field(default=None)

    naziv: Optional[str] = Field(default=None)
    opis: Optional[str] = Field(default=None)
    identifikacijski_broj_mibpg: Optional[str] = Field(default=None)


class KategorijaProizvoda(BaseModel):
    id: int
    naziv: str = Field(min_length=1, max_length=150)
    slug: str

    model_config = {"from_attributes": True}


class Proizvod(BaseModel):
    naziv: str = Field(min_length=1, max_length=200)
    opis: Optional[str] = Field(default=None)
    cijena: Decimal = Field(..., max_digits=12, decimal_places=2)
    slika_proizvoda: Optional[str] = Field(default=None)
    proizvod_dostupan: bool = Field(default=True)
    mjerna_jedinica: str = Field(min_length=1, max_length=50)
    kategorija_id: int

class KreiranjeProizvoda(Proizvod):
    opg_id: int

class AzuriranjeProizvoda(BaseModel):
    naziv: Optional[str] = Field(default=None, min_length=1, max_length=200)
    opis: Optional[str] = Field(default=None)
    cijena: Optional[Decimal] = Field(None, max_digits=12, decimal_places=2)
    slika_proizvoda: Optional[str] = Field(default=None)
    proizvod_dostupan: Optional[bool] = Field(default=None)
    mjerna_jedinica: Optional[str] = Field(default=None, min_length=1, max_length=50)
    kategorija_id: Optional[int] = Field(default=None)

class PrikazProizvoda(Proizvod):
    id: int
    slug: str
    opg_id: int
    
    model_config = {"from_attributes": True}


class KategorijaUsluge(BaseModel):
    id: int
    naziv: str = Field(min_length=1, max_length=150)
    slug: str

    model_config = {"from_attributes": True}


class Usluga(BaseModel):
    naziv: str = Field(min_length=1, max_length=200)
    opis: Optional[str] = Field(default=None)
    cijena: Decimal = Field(..., max_digits=12, decimal_places=2)
    slika_usluge: Optional[str] = Field(default=None)
    usluga_dostupna: bool = Field(default=True)
    mjerna_jedinica: str = Field(min_length=1, max_length=50)
    trajanje_po_mjernoj_jedinici: Optional[int] = Field(default=None, ge=0)
    kategorija_id: int

class KreiranjeUsluge(Usluga):
    opg_id: int

class AzuriranjeUsluge(BaseModel):
    naziv: Optional[str] = Field(default=None, min_length=1, max_length=200)
    opis: Optional[str] = Field(default=None)
    cijena: Optional[Decimal] = Field(None, max_digits=12, decimal_places=2)
    slika_usluge: Optional[str] = Field(default=None)
    usluga_dostupna: Optional[bool] = Field(default=None)
    mjerna_jedinica: Optional[str] = Field(default=None, min_length=1, max_length=50)
    trajanje_po_mjernoj_jedinici: Optional[int] = Field(default=None, ge=0)
    kategorija_id: Optional[int] = Field(default=None)

class PrikazUsluge(Usluga):
    id: int
    slug: str
    opg_id: int
    
    model_config = {"from_attributes": True}

class KreiranjeRecenzije(BaseModel):
    ocjena: int = Field(..., ge=1, le=5)
    komentar: str | None = None

class PrikazRecenzije(BaseModel):
    id: int
    ocjena: int
    komentar: str | None
    korisnik_ime: str | None
    datum_izrade: datetime


class DatumRaspolozivosti(BaseModel):
    datum: date
    pocetno_vrijeme: str = Field(pattern=r"^\d{2}:\d{2}$")
    zavrsno_vrijeme: str = Field(pattern=r"^\d{2}:\d{2}$")
    naslov: Optional[str] = None

class DatumRapolozivostiPrikaz(DatumRaspolozivosti):
    id: int

class RasponKalendaraPrikaz(BaseModel):
    od: str
    do: str
    naslov: Optional[str] = None

class MjeseciKalendaraPrikaz(BaseModel):
    slotovi: dict[str, list[RasponKalendaraPrikaz]]

class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"
    tip_korisnika: Literal["Kupac", "Opg"]


