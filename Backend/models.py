from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Text, String, Boolean, Enum, func, DateTime, UniqueConstraint, Numeric
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

    recenzije = relationship(
        "Recenzija",
        back_populates="korisnik",
        cascade="all, delete-orphan",
        passive_deletes=True
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
    prosjecna_ocjena = Column(Numeric(3, 2), nullable=True)
    broj_recenzija = Column(Integer, default=0)
    
    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False, unique=True) 
    korisnik = relationship("Korisnik", back_populates="opg")
    proizvodi = relationship("Proizvod", back_populates="opg", cascade="all, delete-orphan", passive_deletes=True)
    usluge = relationship("Usluga", back_populates="opg", cascade="all, delete-orphan", passive_deletes=True)

class KategorijaProizvoda(Base):
    __tablename__="kategorije_proizvoda"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String(150), nullable=False, unique=True)
    slug = Column(String(255), nullable=False, unique=True)
    opis = Column(String(500), nullable=True)
    slika_kategorije = Column(String(500), nullable=True)
    datum_izrade = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) 
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    proizvodi = relationship("Proizvod", back_populates="kategorija", passive_deletes=True)


class Proizvod(Base):
    __tablename__="proizvodi"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String(200), nullable=False)
    opis = Column(String(500), nullable=True)
    cijena = Column(Numeric(12,2), nullable=False)
    slika_proizvoda = Column(String(500), nullable=True)
    proizvod_dostupan = Column(Boolean, default=True, nullable=False)
    mjerna_jedinica = Column(String(50), nullable=False)
    slug = Column(String(255), nullable=False)

    datum_izrade = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) 
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    kategorija_id = Column(
        Integer,
        ForeignKey("kategorije_proizvoda.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )


    opg_id = Column(
        Integer,
        ForeignKey("opgovi.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    kategorija = relationship("KategorijaProizvoda", back_populates="proizvodi")
    opg = relationship("Opg", back_populates="proizvodi")

    __table_args__=(
        UniqueConstraint("opg_id", "slug", name="uq_proizvod_opg_slug"),
    )


class KategorijaUsluge(Base):
    __tablename__ = "kategorije_usluga"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String(200), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    datum_izrade = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) 
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    usluge = relationship("Usluga", back_populates="kategorija", passive_deletes=True)

class Usluga(Base):
    __tablename__ = "usluge"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String(200), nullable=False)
    opis = Column(String(500), nullable=True)
    cijena = Column(Numeric(12,2), nullable=False)
    slika_usluge = Column(String(500), nullable=True)
    usluga_dostupna = Column(Boolean, default=True, nullable=False)
    mjerna_jedinica = Column(String(50), nullable=False)
    slug = Column(String(255), nullable=False)

    datum_izrade = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) 
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False) 


    kategorija_id = Column(
        Integer,
        ForeignKey("kategorije_usluga.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )


    opg_id = Column(
        Integer,
        ForeignKey("opgovi.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    kategorija = relationship("KategorijaUsluge", back_populates="usluge")
    opg = relationship("Opg", back_populates="usluge")

    __table_args__=(
        UniqueConstraint("opg_id", "slug", name="uq_usluga_opg_slug"),
    )


class Recenzija(Base):
    __tablename__ = "recenzije"
    
    id = Column(Integer, primary_key=True, index=True)  
    ocjena = Column(Integer, nullable=False)
    komentar = Column(Text, nullable=True)
    datum_izrade = Column(DateTime, server_default=func.now())
    datum_zadnje_izmjene = Column(DateTime, onupdate=func.now())

    opg_id = Column(Integer, ForeignKey("opgovi.id", ondelete="CASCADE"), nullable=False, index=True)
    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False)

    opg = relationship("Opg", backref="recenzije")
    korisnik = relationship("Korisnik", back_populates="recenzije")


    __table_args__=(
        UniqueConstraint("opg_id", "korisnik_id", name="uq_recenzija_opg_korisnik"),
    )