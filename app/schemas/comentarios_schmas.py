from pydantic import BaseModel

# Esquema base para comentarios
class ComentariosBase(BaseModel):
    comentario: str

# Esquema para crear comentarios
class ComentariosCreate(ComentariosBase):
    pass

# Esquema para comentarios con id
class Comentarios(ComentariosBase):
    comentarios_id: int

    # Cambiar orm_mode a from_attributes (Pydantic v2)
    class Config:
        from_attributes = True
