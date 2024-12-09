from sqlalchemy import Column, Integer, String, Date
from app.database.database import Base

class Seguimiento(Base):
    __tablename__ = "seguimiento"

    seguimiento_id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String)
