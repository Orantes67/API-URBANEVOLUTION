from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.database import Base

class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    img_id = Column(Integer, ForeignKey("imagenes.img_id", ondelete="SET NULL"))
    dir_id = Column(Integer, ForeignKey("direccion.dir_id", ondelete="SET NULL"))
    coment_id = Column(Integer, ForeignKey("comentarios.comentarios_id", ondelete="CASCADE"))
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id", ondelete="CASCADE"))
    seguimiento_id = Column(Integer, ForeignKey("seguimiento.seguimiento_id"))
