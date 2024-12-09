from pydantic import BaseModel

class ContrasenaBase(BaseModel):
    contrasena: str

class ContrasenaCreate(ContrasenaBase):
    pass

class Contrasena(ContrasenaBase):
    contrasena_id: int

    class Config:
         from_attributes = True 
