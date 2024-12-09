from pydantic import BaseModel
from datetime import date
from typing import Optional

class PostBase(BaseModel):
    fecha: Optional[date] = None
    titulo: str
    descripcion: Optional[str] = None
    img_id: Optional[int] = None
    dir_id: Optional[int] = None
    coment_id: int
    usuario_id: int
    seguimiento_id: Optional[int] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    post_id: int

    class Config:
         from_attributes = True 
