from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Imagenes(Base):
    __tablename__ = "imagenes"

    img_id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    archivo_oid = Column(Integer, nullable=False)
