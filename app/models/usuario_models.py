from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido_p = Column(String, nullable=False)
    apellido_m = Column(String)
    edad = Column(Integer, nullable=False)
    correo_id = Column(Integer, ForeignKey("correo.correo_id", ondelete="CASCADE"))
    contrasena_id = Column(Integer, ForeignKey("contrasena.contrasena_id", ondelete="CASCADE"))
