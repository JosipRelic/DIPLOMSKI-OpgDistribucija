from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum, func, DateTime
from sqlalchemy.orm import relationship
import enum

class TipKorisnika(str, enum.Enum):
    kupac = "Kupac"
    opg = "Opg"

class Korisnik(Base):
    __tablename__="korisnici"

    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String(100))
    prezime = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    korisnicko_ime = Column(String(50), unique=True, nullable=False)
    lozinka = Column(String(255), nullable=False)
    tip_korisnika = Column(Enum(TipKorisnika), nullable=False)
    broj_telefona = Column(String(20), unique=True)
    datum_pridruzivanja = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # jedan korisnik ima jedan profil, tj 1:1 veza
    korisnicki_profil = relationship(
        "KorisnickiProfil", 
        back_populates="korisnik", 
        uselist=False, 
        cascade="all, delete-orphan"
    )
    
    kupac = relationship(
        "Kupac",
        back_populates="korisnik",
        uselist=False,
        cascade="all, delete-orphan"
    )

    opg = relationship(
        "Opg",
        back_populates="korisnik",
        uselist=False,
        cascade="all, delete-orphan"
    )


class KorisnickiProfil(Base):
    __tablename__="korisnicki_profili"

    id = Column(Integer, primary_key=True, index=True)
    slika_profila = Column(String(255), nullable=True)
    drzava = Column(String(100))
    zupanija = Column(String(100))
    grad = Column(String(100))
    postanski_broj = Column(String(10))
    adresa = Column(String(255))
    datum_pridruzivanja = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False, unique=True)   
    korisnik = relationship("Korisnik", back_populates="korisnicki_profil")
    


class Kupac(Base):
    __tablename__="kupci"

    id = Column(Integer, primary_key=True, index=True)
    datum_pridruzivanja = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)

    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False, unique=True) 
    korisnik = relationship("Korisnik", back_populates="kupac")
    


class Opg(Base):
    __tablename__="opgovi"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String(150))
    opis = Column(String(500))
    verificiran = Column(Boolean, default=False)
    identifikacijski_broj_mibpg = Column(String(50), nullable=False, unique=True)
    datum_pridruzivanja = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)

    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False, unique=True) 
    korisnik = relationship("Korisnik", back_populates="opg")

    