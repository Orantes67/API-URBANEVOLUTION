from sqlalchemy.orm import Session
from app.models.imagenes_models import Imagenes
from app.schemas.imagenes_schmas import ImagenesCreate

def create_imagen(db: Session, imagen_data: ImagenesCreate):
    db_imagen = Imagenes(**imagen_data.dict())
    db.add(db_imagen)
    db.commit()
    db.refresh(db_imagen)
    return db_imagen

def get_imagen(db: Session, img_id: int):
    return db.query(Imagenes).filter(Imagenes.img_id == img_id).first()

def get_imagenes(db: Session):
    return db.query(Imagenes).all()

def delete_imagen(db: Session, img_id: int):
    imagen = get_imagen(db, img_id)
    db.delete(imagen)
    db.commit()
    return {"message": "Imagen deleted successfully"}

def update_imagen(db: Session, img_id: int, imagen_data: dict):
    imagen = get_imagen(db, img_id)
    if not imagen:
        return None
    for key, value in imagen_data.items():
        setattr(imagen, key, value)
    db.commit()
    db.refresh(imagen)
    return imagen
