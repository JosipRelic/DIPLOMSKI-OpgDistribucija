from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import json, io
from config import OPENAI_API

router = APIRouter(prefix="/ai", tags=["AI - Glasovno popunjavanje formi"])

klijent = OpenAI(api_key=OPENAI_API)

class StrukturirajZahtjev(BaseModel):
  tekst: str
  struktura_upita: str

@router.post("/transkribiraj")
async def transkribiraj(audio: UploadFile = File(...)):
  if hasattr(audio, "size") and audio.size and audio.size > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Audio snimka je prevelika (maksimalno 10 MB).")

  sadrzaj = await audio.read()

  buffer = io.BytesIO(sadrzaj)
  buffer.name = "snimka.webm"  

  try:
      kreiranje_transkripcije = klijent.audio.transcriptions.create(
          model="gpt-4o-mini-transcribe",
          file=buffer,
          language="hr",
          temperature=0.2,
          prompt=(
                "Transkribiraj isključivo na hrvatskom jeziku na latinici."             
            ),
      )
      tekst = getattr(kreiranje_transkripcije, "text", "") or getattr(
          kreiranje_transkripcije, "output_text", ""
      )
      return {"tekst": tekst}

  except Exception as e:
      print("Greška pri transkripciji:", e)
      raise HTTPException(status_code=500, detail="Greška pri transkripciji audio zapisa.")
  
@router.post("/strukturiraj")
async def strukturiraj(sz: StrukturirajZahtjev):
  forme_za_strukturiranje = {

    "prijava": {
      "opis": "Popuni email ili korisničko ime i lozinku ako ih korisnik izgovori",
      "polja": ["email_ili_korisnicko_ime", "lozinka"]
    },

    "registracija_kupac": {
      "opis": "Popuni email, korisničko ime, lozinku, potvrdu lozinke, ime, prezime",
      "polja": ["email", "korisnicko_ime", "lozinka", "potvrda_lozinke", "ime", "prezime"]
    },

    "registracija_opg": {
            "opis": "Popuni email, korisničko ime, lozinku, potvrdu lozinke, naziv se odnosi na naziv opga, ime, prezime, te identifikacijski broj mibpg također zvan identifikacijski broj pg-a ili samo identifikacijski broj",
            "polja": ["email", "korisnicko_ime", "lozinka", "potvrda_lozinke", "naziv", "ime", "prezime", "identifikacijski_broj_mibpg"],
        },

    "podaci_za_dostavu": {
        "opis": "Popuni ime, prezime, email, telefon, adresu, državu, županiju, grad i poštanski broj",
        "polja": ["ime", "prezime", "email", "telefon", "adresa", "drzava", "zupanija", "grad", "postanski_broj"],
    },

    "postavke_kupac": {
        "opis": "Popuni izmijenjena polja: ime, prezime, broj telefona, državu, županiju, grad, poštanski broj, adresu",
        "polja": ["ime", "prezime", "broj_telefona", "drzava", "zupanija", "grad", "postanski_broj", "adresu"],
    },

    "postavke_opg": {
        "opis": "Popuni izmijenjena polja: ime, prezime, broj telefona, državu, županiju, grad, poštanski broj, adresu, naziv se tiče naziva opg-a, opis se tiče opisa opg-a, te identifikacijski broj mibpg",
        "polja": ["ime", "prezime", "broj_telefona", "drzava", "zupanija", "grad", "postanski_broj", "adresa", "naziv", "opis", "identifikacijski_broj_mibpg"],
    },

    "mail_narudzba": {
        "opis": "Popuni predmet i poruku za slanje emaila.",
        "polja": ["predmet", "poruka"],
    },

    "novi_proizvod": {
        "opis": "Popuni naziv proizvoda, opis, cijenu, mjernu jedinicu, da li je proizvod dostupan (true/false), kategoriju, kategorija_id ostavi prazno ili zanemari",
        "polja": ["naziv", "opis", "cijena", "mjerna_jedinica", "proizvod_dostupan", "kategorija", "kategorija_id"],
    },

    "nova_usluga": {
        "opis": "Popuni naziv usluge, opis, cijenu, mjernu jedinicu, da li je usluga dostupna (true/false), kategoriju, kategorija_id ostavi prazno ili zanemari, trajanje po mjernoj jedinici u minutama",
        "polja": ["naziv","opis","cijena","mjerna_jedinica","usluga_dostupna","kategorija", "kategorija_id","trajanje_po_mjernoj_jedinici"],
    },

  }

  strukturirani_json = forme_za_strukturiranje.get(sz.struktura_upita, {"opis": "Vrati strukturirani json od govora.", "polja": []})

  prazno = {k: None for k in strukturirani_json["polja"]}

  upute = f"""
    Pretvori korisnikov govor u strukturirani json za popunjavanje forme "{sz.struktura_upita}".
    Opis: {strukturirani_json["opis"]}
    Vrati isključivo json objekt sa sljedećim ključevima:
    {strukturirani_json["polja"]}
    Ako nešto nije spomenuto, postavi na null ne izostavljaj ključ.
    Ako korisnik govori "promijeni, ispravi ili umjesto", vrati samo ona polja koja treba ažurirati.
    Jezik izlaza mora biti hrvatski (latinica).
    Tekst:
    {sz.tekst}
    """
  
  upit = klijent.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Odgovaraj isključivo kao čisti json bez dodatnog teksta."},
      {"role": "user", "content": upute}
    ]
  )

  odgovor_na_upit = upit.choices[0].message.content or "{}"
  try:
    podaci = json.loads(odgovor_na_upit)
  except Exception:
    podaci = {}

  
  rezultat = {**prazno, **podaci}
 
  return {"podaci": rezultat}


  
