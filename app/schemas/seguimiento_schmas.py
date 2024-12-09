from pydantic import BaseModel
from datetime import date
from typing import Optional

class SeguimientoBase(BaseModel):
    status: str
    fecha: date
    descripcion: Optional[str] = None

class SeguimientoCreate(SeguimientoBase):
    pass

class Seguimiento(SeguimientoBase):
    seguimiento_id: int

    class Config:
         from_attributes = True 
