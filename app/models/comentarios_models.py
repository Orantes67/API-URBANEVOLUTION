from sqlalchemy import Column, Integer, String,ForeignKey
from app.database.database import Base

class Comentarios(Base):
    __tablename__ = "comentarios"

    comentarios_id = Column(Integer, primary_key=True, index=True)
    comentario = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("post.post_id", ondelete="CASCADE"))  # Nueva columna