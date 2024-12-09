from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Direccion(Base):
    __tablename__ = "direccion"

    dir_id = Column(Integer, primary_key=True, index=True)
    direccion = Column(String, nullable=False)
