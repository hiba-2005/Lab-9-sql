from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Date
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "VotreMdp")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "universite")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}",
    echo=False,
    future=True
)
Session = sessionmaker(bind=engine, future=True)
Base = declarative_base()

class Etudiant(Base):
    __tablename__ = "ETUDIANT"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)

    inscriptions = relationship("Inscription", back_populates="etudiant")

class Cours(Base):
    __tablename__ = "COURS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titre = Column(String(200), nullable=False)
    credits = Column(Integer, nullable=False, default=3)

    inscriptions = relationship("Inscription", back_populates="cours")

class Inscription(Base):
    __tablename__ = "INSCRIPTION"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_inscription = Column(Date, nullable=False)

    etudiant_id = Column(Integer, ForeignKey("ETUDIANT.id"), nullable=False)
    cours_id = Column(Integer, ForeignKey("COURS.id"), nullable=False)

    etudiant = relationship("Etudiant", back_populates="inscriptions")
    cours = relationship("Cours", back_populates="inscriptions")
