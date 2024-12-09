from pydantic import BaseModel

class ImagenesBase(BaseModel):
    tipo: str
    archivo_oid: int

class ImagenesCreate(ImagenesBase):
    pass

class Imagenes(ImagenesBase):
    img_id: int

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes
