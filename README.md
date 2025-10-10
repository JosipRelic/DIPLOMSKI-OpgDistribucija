# DIPLOMSKI-OpgDistribucija

Ovaj repozitorij je napravljen za diplomski rad na temu Glasovno popunjavanje formi pomoću obrade prirodnog jezika i prepoznavanja imenovanih entiteta. Napravio sam aplikaciju zvanu OPG Distribucija koja će služiti lokalnim OPG-ovima za prodaju vlastitih proizvoda i ponude usluga. Unutar aplikacije sam implementirao glasovno popunjavanje formi što je ujedno i glavni dio ovog diplomskog rada.

Tehnologije: VUE3+pinia, FastAPI, PostgreSQL, OpenAI Whisper za speech to text, OpenAI GPT 4o mini za strukturirane output-e.

Verzije korištene u projektu (potrebno instalirati ukoliko nemate): - Node.js v22.15.0 - Python 3.11.2 - PostgreSQL Version 16, pgadmin4

Pokretanje frontenda:

1. otvoriti root folder projekta u git bash terminalu (ili vs code)
2. cd Frontend
3. npm install
4. u Frontend folderu napraviti .env fajl s
   VITE_API_URL=dodati_url_localhosta
5. npm run dev
6. otvoriti app u browseru (localhost+port link u terminalu)

Pokretanje backenda:

1.  Instalirati pgadmin4 i postgresql i kreirati bazu podataka
2.  otvoriti root folder projekta u git bash terminalu
3.  cd Backend
4.  Kreirati virtualno okruženje unutar kojeg ćemo izolirati i instalirati sve pakete o kojima projekt ovisi (OBAVEZNO RADITI UNUTAR VENV radi mogućih konflikta s vašim lokalno instaliranim paketima):
    ► pip install virtualenv (ukoliko nemate instaliran virtualenv na svom računalu... s pip list možete provjeriti sve lokalno instalirane pakete)

    ► kreiranja venv i instalacija paketa:

    - unutar Backend foldera kreirajte virtualno okruženje s komandom -> python -m venv venv
    - nakon toga aktivirajte virtualno okruženje s komandom -> source venv/Scripts/activate (WINDOWS) ili source venv/bin/activate (MAC)
    - nakon aktiviranja pojavit će se (venv) u terminalu što je znak da je virtualno okruženje aktivirano možemo provjeriti s pip list i uvjeriti se da nemam instaliranih paketa u venv
    - nakon aktivacije venv-a unutar njega ćemo instalirati pakete o kojima ovisi backend sa pip install -r requirements.txt
    - provjerimo sve pakete unutar venv s pip list

5.  unutar Backend foldera kreiramo .env fajl s varijablama:

                DB_USER=naziv_usera_u_bazi
                DB_PASSWORD=lozinka_baze
                DB_HOST=dodati_host
                DB_PORT=dodati_port
                DB_NAME=naziv_baze_koju_ste_kreirali
                SECRET_KEY=dodati secret key -> generirati s komandom u gitbash terminalu python -c "import secrets; print(secrets.token_hex(32))"
                ALGORITHM=HS256
                ACCESS_TOKEN_EXPIRE_MINUTES=dodati_vrijeme_u_minutama_integer
                SMTP_SERVER=server
                SMTP_PORT=port
                SMTP_USERNAME=korisnicko_ime
                SMTP_PASSWORD=lozinka
                FRONTEND_URL=frontend_url
                BACKEND_URL=backend_url
                ADMIN_USER=adminuser
                ADMIN_PASS=adminpass

6.  kreiranje svih tablica u bazi s alembicom komandom -> alembic upgrade head
7.  pokretanje backenda s -> uvicorn app:main --reload
8.  otvoriti app u browseru (localhost + port u terminalu)
