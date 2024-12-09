from pydantic import BaseModel

class DireccionBase(BaseModel):
    direccion: str

class DireccionCreate(DireccionBase):
    pass

class Direccion(DireccionBase):
    dir_id: int

    class Config:
         from_attributes = True 
