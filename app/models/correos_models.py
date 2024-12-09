from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Correo(Base):
    __tablename__ = "correo"

    correo_id = Column(Integer, primary_key=True, index=True)
    correo = Column(String, nullable=False, unique=True)
