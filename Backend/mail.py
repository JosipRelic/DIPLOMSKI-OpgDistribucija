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

def posalji_email_za_oporavak(email:str, reset_token:str):
    reset_link = f"{FRONTEND_URL}/promjena-lozinke?token={reset_token}"

    subject = "Zahtjev za promjenu lozinke"
    html_content = f"""
    <html>
        <body>
            <h2>Pozdrav!</h2>
            <p>Zatražili ste promjenu lozinke. Kliknite na poveznicu ispod kako biste postavili novu lozinku:</p>
            <a href="{reset_link}" style="background:#008080;color:white;padding:10px 20px;text-decoration:none;border-radius:5px;">
                Promijeni lozinku
            </a>
            <p>Ova poveznica vrijedi 30 minuta.</p>
            <p>Ako niste vi zatražili promjenu, jednostavno ignorirajte ovu poruku. Vaša OPG Distribucija.</p>
        </body>
    </html>
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = email
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [email], msg.as_string())