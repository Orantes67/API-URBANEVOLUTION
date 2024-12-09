from pydantic import BaseModel, EmailStr

class CorreoBase(BaseModel):
    correo: EmailStr

class CorreoCreate(CorreoBase):
    pass

class Correo(CorreoBase):
    correo_id: int

    class Config:
         from_attributes = True 
