from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Contrasena(Base):
    __tablename__ = "contrasena"

    contrasena_id = Column(Integer, primary_key=True, index=True)
    contrasena = Column(String, nullable=False)
