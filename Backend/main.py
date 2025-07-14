from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session 
from sqlalchemy import text #izbrisati ovo i tablicu u bazi kad završim test
from database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def test_baze(db: Session = Depends(get_db)):
    select = db.execute(text("SELECT * FROM test_tablica"))
    rez = select.mappings().fetchall()
    return rez



