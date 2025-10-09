from email.mime.image import MIMEImage
from email.utils import formataddr
import html
import imghdr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER=os.getenv("SMTP_SERVER")
SMTP_PORT=os.getenv("SMTP_PORT")
SMTP_USERNAME=os.getenv("SMTP_USERNAME")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")
FRONTEND_URL=os.getenv("FRONTEND_URL")
BACKEND_URL=os.getenv("BACKEND_URL")

def _attach_logo(msg, cid="logo_opg"):
   
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "assets", "logo_opgdistribucija.jpg"),
        os.path.join(os.getcwd(), "static", "assets", "logo_opgdistribucija.jpg"),
    ]
    logo_path = next((p for p in candidates if os.path.isfile(p)), None)
    if not logo_path:
        print("Logo nije pronađen ni u jednoj od očekivanih putanja:", candidates)
        return

    try:
        with open(logo_path, "rb") as f:
            data = f.read()
        subtype = imghdr.what(None, h=data) or "jpeg"  
        img = MIMEImage(data, _subtype=subtype)
        img.add_header("Content-ID", f"<{cid}>")
        img.add_header("Content-Disposition", "inline", filename=os.path.basename(logo_path))
        msg.attach(img)
    except Exception as e:
        print("Logo se nije mogao pridružiti mailu:", e)


def posalji_email_za_oporavak(email: str, reset_token: str):
    reset_link = f"{FRONTEND_URL}/promjena-lozinke?token={reset_token}"

    subject = "🔒 Oporavak lozinke - OPG Distribucija"

    header_logo = """
    <div style="text-align:center;padding:16px 0;">
        <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:60px;display:block;margin:0 auto 8px auto;">
        <div style="font-size:14px;color:#666;">OPG Distribucija</div>
    </div>
    """

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:600px;margin:auto;background:white;border-radius:10px;overflow:hidden;border:1px solid #e5e5e5;">
            {header_logo}
            <div style="background-color:#008080;color:white;padding:20px;text-align:center;">
                <h2>Zahtjev za promjenu lozinke</h2>
            </div>
            <div style="padding:25px;">
                <p>Pozdrav,</p>
                <p>Zaprimili smo zahtjev za promjenu lozinke vašeg računa na <b>OPG Distribuciji</b>.</p>
                <p>Kliknite na gumb ispod kako biste postavili novu lozinku:</p>

                <div style="text-align:center;margin:30px 0;">
                    <a href="{reset_link}" style="background:#008080;color:white;padding:12px 24px;text-decoration:none;border-radius:6px;font-weight:bold;">
                        🔑 Promijeni lozinku
                    </a>
                </div>

                <p>Ova poveznica vrijedi <b>30 minuta</b>. Nakon isteka, morat ćete zatražiti novu.</p>
                <p>Ukoliko niste vi zatražili ovu promjenu, možete sigurno ignorirati ovu poruku.</p>

                <hr style="margin:30px 0;border:none;border-top:1px solid #eee;">
                <p style="font-size:13px;color:#777;">
                    OPG Distribucija • Podržite domaće proizvođače 🌿<br>
                    Ova poruka je automatski generirana - molimo ne odgovarajte na nju.
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html"))
    msg.attach(alt)
    _attach_logo(msg)

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [email], msg.as_string())


def posalji_email_narudzbe_narucitelju(email: str, narudzba):
    subject = f"✅ Potvrda vaše narudžbe #{narudzba.broj_narudzbe}"

    stavke_html = ""
    for s in narudzba.stavke:
        stavke_html += f"""
        <tr>
            <td>{s.naziv}</td>
            <td>{int(s.kolicina or 0)} {s.mjerna_jedinica or ''}</td>
            <td style="text-align:right;">{float(s.cijena or 0):.2f} €</td>
        </tr>
        """

    
    header_logo = """
    <div style="text-align:center;padding:16px 0;">
        <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
        <div style="font-size:14px;color:#666;">OPG Distribucija</div>
    </div>
    """

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color:#333;">
        <div style="max-width:600px;margin:auto;border:1px solid #eee;border-radius:10px;overflow:hidden;">
            {header_logo}
            <div style="background-color:#223c2f;color:white;padding:20px;text-align:center;">
                <h2>Hvala na vašoj narudžbi!</h2>
                <p>Vaša narudžba #{narudzba.broj_narudzbe} je uspješno zaprimljena.</p>
            </div>
            <div style="padding:20px;">
                <h3>Pregled narudžbe:</h3>
                <table border="0" cellpadding="8" cellspacing="0" style="width:100%;border-collapse:collapse;">
                    <tr style="background-color:#f0f0f0;text-align:left;">
                        <th>Proizvod / Usluga</th>
                        <th>Količina</th>
                        <th style="text-align:right;">Cijena</th>
                    </tr>
                    {stavke_html}
                </table>
                <hr>
                <p><b>Iznos bez PDV-a:</b> {float(narudzba.iznos_bez_pdva or 0):.2f} €<br>
                <b>PDV:</b> {float(narudzba.pdv or 0):.2f} €<br>
                <b>Dostava:</b> {float(narudzba.dostava or 0):.2f} €<br>
                <b>Ukupno:</b> {float(narudzba.ukupno or 0):.2f} €</p>
                <hr>
                <h3>Adresa za dostavu:</h3>
                <p>👤 {narudzba.ime} {narudzba.prezime}<br>
                📍{narudzba.adresa}, {narudzba.grad} {narudzba.postanski_broj} <br> 
                {narudzba.zupanija}, {narudzba.drzava}<br>
                📞 {narudzba.telefon} | ✉️ {narudzba.email}</p>

                <p><b>Način plaćanja:</b> {narudzba.nacin_placanja}<br>
                <b>Način dostave:</b> {narudzba.nacin_dostave}</p>
            </div>
            <div style="background-color:#f8f8f8;color:#666;text-align:center;padding:10px;font-size:12px;">
                OPG Distribucija - Hvala što podržavate domaće proizvođače 🌿 <br>
                Pregled narudžbe u vašem profilu -> "OPG - Napravljene narudžbe, KUPAC - Moje narudžbe"
            </div>
        </div>
    </body>
    </html>
    """

    msg = MIMEMultipart("related")  
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html"))
    msg.attach(alt)
    _attach_logo(msg)  

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [email], msg.as_string())


def posalji_email_narudzbe_opg_primatelju(opg_email: str, opg_naziv: str, stavke, broj_narudzbe: str, kupac, narudzba):
    subject = f"📦 Nova narudžba #{broj_narudzbe} - {kupac['ime']} {kupac['prezime']}"

    
    stavke_html = ""
    meduzbroj = 0.0
    for s in stavke:
        k = int(s.kolicina or 0)
        c = float(s.cijena or 0)
        meduzbroj += k * c
        stavke_html += f"""
        <tr>
            <td>{s.naziv}</td>
            <td>{k} {s.mjerna_jedinica or ''}</td>
            <td style="text-align:right;">{c:.2f} €</td>
        </tr>
        """

   
    dostava_opg = 5.0 if (str(narudzba.nacin_dostave or "").lower() == "dostava") else 0.0
    ukupno_opg = meduzbroj + dostava_opg

    header_logo = """
    <div style="text-align:center;padding:16px 0;">
        <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
        <div style="font-size:14px;color:#666;">OPG Distribucija</div>
    </div>
    """

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color:#333;">
        <div style="max-width:600px;margin:auto;border:1px solid #eee;border-radius:10px;overflow:hidden;">
            {header_logo}
            <div style="background-color:#223c2f;color:white;padding:20px;text-align:center;">
                <h2>Nova narudžba #{broj_narudzbe}</h2>
                <p>Zaprimili ste novu narudžbu putem OPG Distribucije</p>
            </div>
            <div style="padding:20px;">
                <h3>Podaci o kupcu:</h3>
                <p>
                    👤 <b>{kupac['ime']} {kupac['prezime']}</b><br>
                    ✉️ {kupac['email']}<br>
                    📞 {kupac['telefon']}<br>
                    📍 {kupac['adresa']}<br>
                    {kupac['zupanija']}, {kupac['drzava']}
                </p>

                <hr>
                <h3>Stavke narudžbe:</h3>
                <table border="0" cellpadding="8" cellspacing="0" style="width:100%;border-collapse:collapse;">
                    <tr style="background-color:#f0f0f0;text-align:left;">
                        <th>Proizvod / Usluga</th>
                        <th>Količina</th>
                        <th style="text-align:right;">Cijena</th>
                    </tr>
                    {stavke_html}
                </table>

                <hr>
                <p><b>Način plaćanja:</b> {narudzba.nacin_placanja}<br>
                <b>Način dostave:</b> {narudzba.nacin_dostave}</p>

                <p>
                    <b>Međuzbroj (vaše stavke):</b> {meduzbroj:.2f} €<br>
                    <b>Dostava:</b> {dostava_opg:.2f} €<br>
                    <b>Ukupno:</b> {ukupno_opg:.2f} €
                </p>
            </div>
            <div style="background-color:#f8f8f8;color:#666;text-align:center;padding:10px;font-size:12px;">
                OPG Distribucija - Pregled narudžbe u vašem profilu -> "Primljene narudžbe"
            </div>
        </div>
    </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html"))
    msg.attach(alt)
    _attach_logo(msg)

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = opg_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [opg_email], msg.as_string())


def opg_posalji_email_vezan_uz_narudzbu(
    kupac_email: str,
    kupac_ime_prezime: str,
    opg_naziv: str,
    broj_narudzbe: str,
    predmet: str,
    poruka_plain: str,
):
   
    body_html = html.escape(poruka_plain or "").replace("\n", "<br>")

    full_subject = f"[{opg_naziv}] {predmet} - Narudžba #{broj_narudzbe}"

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:640px;margin:auto;border:1px solid #eee;border-radius:12px;overflow:hidden;background:white;">
          <div style="background:#223c2f;padding:16px 20px;display:flex;align-items:center;gap:12px;color:#fff;">
            <img src="cid:logo_opg" alt="OPG Distribucija" height="36" style="display:block;border-radius:6px;margin-right:2px;" />
            <div>
              <div style="font-weight:700;">OPG Distribucija</div>
              <div style="opacity:.9;font-size:13px;">Poruka od: {html.escape(opg_naziv)}</div>
            </div>
          </div>
          <div style="padding:22px;">
            <h2 style="margin:0 0 8px 0;">Vezano uz narudžbu: #{broj_narudzbe}</h2>
            <p style="margin:0 0 18px 0;">Poštovani/na {html.escape(kupac_ime_prezime)},</p>
            <div style="border:1px solid #eee;border-radius:10px;padding:14px 16px;background:#fafafa;">
              {body_html}
            </div>
            <p style="margin:18px 0 0 0;font-size:13px;color:#555;">
              Ovu poruku Vam šalje <b>{html.escape(opg_naziv)}</b> putem platforme OPG Distribucija.
            </p>
          </div>
          <div style="background:#f8f8f8;color:#666;text-align:center;padding:10px;font-size:12px;">
            OPG Distribucija - Hvala što podržavate domaće proizvođače 🌿
          </div>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("related")
    msg["Subject"] = full_subject
    msg["From"] = formataddr((f"{opg_naziv} putem OPG Distribucije", SMTP_USERNAME))
    msg["To"] = kupac_email

    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText("Poruka vezano uz vašu narudžbu na OPG Distribucija.", "plain", "utf-8"))
    alt.attach(MIMEText(html_content, "html", "utf-8"))
    msg.attach(alt)

    
    try:
      _attach_logo(msg, cid="logo_opg")
    except Exception as e:
      print("Logo se nije mogao pridružiti:", e)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [kupac_email], msg.as_string())


def posalji_email_o_promjeni_statusa_kupcu(
    kupac_email: str,
    kupac_ime_prezime: str,
    broj_narudzbe: str,
    opg_naziv: str,
    novi_status: str,
):
   
    STATUS_LABEL = {
        "u_tijeku": "U tijeku",
        "isporuceno": "Isporučeno",
        "otkazano": "Otkazano",
    }
    status_label = STATUS_LABEL.get((novi_status or "").strip().lower(), novi_status)

    subject = f"📝 Ažuriranje statusa #{broj_narudzbe} - {opg_naziv}"

    header_logo = """
    <div style="text-align:center;padding:16px 0;">
        <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
        <div style="font-size:14px;color:#666;">OPG Distribucija</div>
    </div>
    """

    aplikacija_link = FRONTEND_URL or "#"

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:640px;margin:auto;border:1px solid #eee;border-radius:12px;overflow:hidden;background:white;">
          {header_logo}
          <div style="background:#223c2f;color:#fff;padding:20px;text-align:center;">
            <h2>Obavijest o promjeni statusa</h2>
            <p style="margin:6px 0 0 0;">Narudžba #{broj_narudzbe}</p>
          </div>
          <div style="padding:22px;">
            <p style="margin:0 0 10px 0;">Poštovani/na {html.escape(kupac_ime_prezime)},</p>
            <p style="margin:0 0 12px 0;">
              <b>{html.escape(opg_naziv)}</b> je ažurirao status svojih stavki u vašoj narudžbi.
            </p>
            <div style="border:1px solid #eee;border-radius:10px;padding:14px 16px;background:#fafafa;margin:12px 0;">
              <b>Novi status:</b> {html.escape(status_label)}
            </div>

            <div style="text-align:center;margin:24px 0;">
              <a href="{aplikacija_link}" style="background:#008080;color:white;padding:12px 22px;text-decoration:none;border-radius:8px;font-weight:600;">
                Otvori aplikaciju
              </a>
            </div>

           
          </div>
          <div style="background:#f8f8f8;color:#666;text-align:center;padding:10px;font-size:12px;">
            OPG Distribucija - Hvala što podržavate domaće proizvođače 🌿
          </div>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText("Promjena statusa vaše narudžbe.", "plain", "utf-8"))
    alt.attach(MIMEText(html_content, "html", "utf-8"))
    msg.attach(alt)
    _attach_logo(msg)

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = kupac_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [kupac_email], msg.as_string())



def posalji_email_zahvale_za_registraciju_opgu(email: str, ime: str, prezime: str, naziv_opg: str):
    subject = "🎉 Hvala na registraciji - OPG Distribucija"

    header_logo = """
    <div style="text-align:center;padding:16px 0;">
        <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
        <div style="font-size:14px;color:#666;">OPG Distribucija</div>
    </div>
    """

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:640px;margin:auto;border:1px solid #eee;border-radius:12px;overflow:hidden;background:white;">
          {header_logo}
          <div style="background:#223c2f;color:#fff;padding:20px;text-align:center;">
            <h2 style="margin:0;">Hvala na registraciji!</h2>
            <p style="margin:6px 0 0 0;">Vaš OPG čeka verifikaciju</p>
          </div>
          <div style="padding:22px;">
            <p>Pozdrav {(ime or '').strip()} {(prezime or '').strip()},</p>
            <p>Zaprimili smo vašu registraciju za <b>{html.escape(naziv_opg or 'OPG')}</b>.</p>
            <p>Kako biste pristupili vašem računu i svim funkcionalnostima platforme, potrebno je pričekati verifikaciju od strane administratora. Nakon uspješne verifikacije poslat ćemo vam obavijest e-poštom.</p>
            <p>Hvala na strpljenju i dobro došli na <b>OPG Distribuciju</b>! 🌿</p>
            <hr style="margin:24px 0;border:none;border-top:1px solid #eee;">
            <p style="font-size:12px;color:#666;text-align:center;">
              OPG Distribucija • Podržite domaće proizvođače
            </p>
          </div>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html", "utf-8"))
    msg.attach(alt)
    _attach_logo(msg, cid="logo_opg")

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [email], msg.as_string())



def posalji_email_adminu_novi_opg_registriran(opg_id: int, naziv_opg: str, ime: str, prezime: str, email_opg: str, mibpg: str):
    
    verify_link = f"{BACKEND_URL}/autentifikacija/verificiraj-opg/{opg_id}"
    subject = f"Novi OPG za verifikaciju: {naziv_opg}"

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:640px;margin:auto;border:1px solid #eee;border-radius:12px;overflow:hidden;background:white;">
          <div style="text-align:center;padding:16px 0;background:#223c2f;color:#fff;">
            <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
            <h2 style="margin:0;">Novi OPG čeka verifikaciju</h2>
          </div>
          <div style="padding:22px;">
            <p><b>Naziv:</b> {html.escape(naziv_opg or '—')}</p>
            <p><b>MIBPG:</b> {html.escape(mibpg or '—')}</p>
            <p><b>Vlasnik:</b> {html.escape(ime or '')} {html.escape(prezime or '')}</p>
            <p><b>Email:</b> {html.escape(email_opg or '')}</p>
            <p style="margin-top:20px;">Za verifikaciju kliknite:</p>
            <p><a href="{verify_link}" style="background:#008080;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Verificiraj OPG</a></p>
          </div>
          <hr style="border:none;border-top:1px solid #eee;margin:20px 0;">
          <p style="font-size:12px;color:#666;text-align:center;">OPG Distribucija - Administratorska obavijest</p>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html", "utf-8"))
    msg.attach(alt)
    _attach_logo(msg, cid="logo_opg")

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = SMTP_USERNAME  

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [SMTP_USERNAME], msg.as_string())



def posalji_email_opg_verificiran(email_opg: str, naziv_opg: str):
    subject = "✅ Vaš OPG je verificiran!"

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333; padding:20px;">
        <div style="max-width:640px;margin:auto;border:1px solid #eee;border-radius:12px;overflow:hidden;background:white;">
          <div style="text-align:center;padding:16px 0;background:#223c2f;color:#fff;">
            <img src="cid:logo_opg" alt="OPG Distribucija" style="max-height:56px;display:block;margin:0 auto 8px auto;">
            <h2 style="margin:0;">Vaš OPG je verificiran!</h2>
          </div>
          <div style="padding:22px;">
            <p>Pozdrav,</p>
            <p>Vaš <b>{html.escape(naziv_opg or '')}</b> uspješno je verificiran i sada možete pristupiti svom računu na platformi <b>OPG Distribucija</b>.</p>
            <p><a href="{FRONTEND_URL}/prijava" style="background:#008080;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;margin-top:4px;margin-bottom:4px;">Prijavite se</a></p>
            <p>Hvala što ste dio naše zajednice!</p>
          </div>
          <hr style="border:none;border-top:1px solid #eee;margin:20px 0;">
          <p style="font-size:12px;color:#666;text-align:center;">OPG Distribucija - Podržite domaće proizvođače</p>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("related")
    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(html_content, "html", "utf-8"))
    msg.attach(alt)
    _attach_logo(msg, cid="logo_opg")

    msg["Subject"] = subject
    msg["From"] = formataddr(("OPG Distribucija", SMTP_USERNAME))
    msg["To"] = email_opg

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [email_opg], msg.as_string())