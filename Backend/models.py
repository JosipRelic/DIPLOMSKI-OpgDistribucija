from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Text, String, Boolean, Enum, func, DateTime, UniqueConstraint, Numeric, Date, CheckConstraint, Index
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
    trajanje_po_mjernoj_jedinici = Column(Integer, nullable=True)
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


class OpgRaspolozivostPoDatumu(Base):
    __tablename__ = "opgovi_raspolozivost_po_datumu"

    id = Column(Integer, primary_key=True)
    
    datum = Column(Date, nullable=False)
    pocetno_vrijeme = Column(Integer, nullable=False)
    zavrsno_vrijeme = Column(Integer, nullable=False)
    naslov = Column(String(200), nullable=True)

    opg_id = Column(Integer, ForeignKey("opgovi.id", ondelete="CASCADE"), index=True, nullable=False)
    
    opg = relationship("Opg", backref="raspolozivost_po_datumu") 

    __table_args__ = (
        CheckConstraint("pocetno_vrijeme < zavrsno_vrijeme", name="ck_raspolozivost_ispravan_raspon"),

        UniqueConstraint("opg_id", "datum", "pocetno_vrijeme", "zavrsno_vrijeme", name="uq_opg_datum_poc_kraj"),

        Index("ix_raspolozivost_opg_datum", "opg_id", "datum"),
    )


class KosaricaStavka(Base):
    __tablename__ = "kosarica_stavke"

    id = Column(Integer, primary_key=True)
    kolicina = Column(Integer, nullable=False)
    termin_od = Column(String(50), nullable=True)
    termin_do = Column(String(50), nullable=True)
    cijena = Column(Numeric(12,2), nullable=False)
    mjerna_jedinica = Column(String(50), nullable=False)
    datum_izrade = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    datum_zadnje_izmjene = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    korisnik_id = Column(Integer, ForeignKey("korisnici.id", ondelete="CASCADE"), nullable=False, index=True)
    proizvod_id = Column(Integer, ForeignKey("proizvodi.id", ondelete="CASCADE"), nullable=True, index=True)
    usluga_id = Column(Integer, ForeignKey("usluge.id", ondelete="CASCADE"), nullable=True, index=True)

    proizvod = relationship("Proizvod")
    usluga = relationship("Usluga")

    __table_args__=(
        CheckConstraint(
            "(proizvod_id IS NOT NULL AND usluga_id IS NULL) OR (proizvod_id IS NULL AND usluga_id IS NOT NULL)",
            name="ck_kos_xor_proizvod_usluga"
            ),
        UniqueConstraint("korisnik_id", "proizvod_id", name="uq_kos_proizvod_po_korisniku"),
        UniqueConstraint("korisnik_id", "usluga_id", "termin_od", "termin_do", name="uq_kos_usluga_termin_po_korisniku"),
        Index("ix_kos_korisnik_tip", "korisnik_id", "proizvod_id", "usluga_id"),
    )


class Narudzba(Base):
    __tablename__ = "narudzbe"
    
    id = Column(Integer, primary_key=True, index=True)
    broj_narudzbe = Column(String, unique=True, index=True)
    ime = Column(String, nullable=False)
    prezime = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefon = Column(String, nullable=False)
    adresa = Column(String, nullable=False)
    grad = Column(String, nullable=False)
    postanski_broj = Column(String, nullable=False)
    zupanija = Column(String, nullable=False)
    drzava = Column(String, nullable=False)
    nacin_placanja = Column(String, default="pouzece")
    nacin_dostave = Column(String, default="osobno")
    iznos_bez_pdva = Column(Numeric(10,2))
    pdv = Column(Numeric(10,2))
    dostava = Column(Numeric(10,2))
    ukupno = Column(Numeric(10,2))
    datum_izrade = Column(DateTime, server_default=func.now()) 

    korisnik_id = Column(
        Integer,
        ForeignKey("korisnici.id", ondelete="SET NULL"),
        nullable=True,  
        index=True
    )

    stavke = relationship("NarudzbaStavka", back_populates="narudzba", cascade="all, delete-orphan")


class NarudzbaStavka(Base):
    __tablename__ = "narudzba_stavke"

    id = Column(Integer, primary_key=True, index=True)
    tip = Column(String, nullable=False) #proizvod ili usluga
    naziv = Column(String, nullable=False)
    kolicina = Column(Integer, nullable=False)
    mjerna_jedinica = Column(String, nullable=True)
    cijena = Column(Numeric(10,2), nullable=False)
    slika = Column(String, nullable=True)
    termin_od = Column(DateTime, nullable=True)
    termin_do = Column(DateTime, nullable=True)

    narudzba_id = Column(Integer, ForeignKey("narudzbe.id"))

    narudzba = relationship("Narudzba", back_populates="stavke")