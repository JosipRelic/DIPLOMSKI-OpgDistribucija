from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SMTP_SERVER=os.getenv("SMTP_SERVER")
SMTP_PORT=os.getenv("SMTP_PORT")
SMTP_USERNAME=os.getenv("SMTP_USERNAME")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")
FRONTEND_URL=os.getenv("FRONTEND_URL")
BACKEND_URL=os.getenv("BACKEND_URL")

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")
OPENAI_API=os.getenv("OPENAI_API")