from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellido_p: str
    apellido_m: Optional[str] = None
    edad: int
    correo_id: int
    contrasena_id: int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    usuario_id: int

    class Config:
         from_attributes = True 
