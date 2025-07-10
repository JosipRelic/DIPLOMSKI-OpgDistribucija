from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from sqlalchemy import text #izbrisati ovo i tablicu u bazi kad završim test
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def prva_poruka():
    return {"poruka": "FastAPI radi"}

@app.get("/test-baze")
def test_baze(db: Session = Depends(get_db)):
    select = db.execute(text("SELECT * FROM test_tablica"))
    rez = select.mappings().fetchall()
    return rez