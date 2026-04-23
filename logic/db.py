from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Monitor(Base):
    __tablename__ = "Monitor"
    id          = Column(Integer, primary_key=True, autoincrement=True)
    url         = Column(String)
    estado      = Column(String)   # "online" o "offline"
    codigo_http = Column(Integer)  # 200, 404, 500, etc.
    tiempo_ms   = Column(Integer)  # tiempo de respuesta en milisegundos
    chequeado_en = Column(DateTime, default=datetime.utcnow)
    
Base.metadata.create_all(bind=engine)