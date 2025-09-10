from pydantic import BaseModel, Field, EmailStr
from decimal import Decimal
from typing import Literal, Optional

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


class Token(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"
    tip_korisnika: Literal["Kupac", "Opg"]
    