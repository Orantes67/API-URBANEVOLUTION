from sqlalchemy.orm import Session
from app.models.correos_models import Correo
from app.schemas.correos_schmas import CorreoCreate

def create_correo(db: Session, correo_data: CorreoCreate):
    db_correo = Correo(**correo_data.dict())
    db.add(db_correo)
    db.commit()
    db.refresh(db_correo)
    return db_correo

def get_correo(db: Session, correo_id: int):
    return db.query(Correo).filter(Correo.correo_id == correo_id).first()

def get_correos(db: Session):
    return db.query(Correo).all()

def delete_correo(db: Session, correo_id: int):
    correo = get_correo(db, correo_id)
    db.delete(correo)
    db.commit()
    return {"message": "Correo deleted successfully"}

def update_correo(db: Session, correo_id: int, correo_data: dict):
    correo = get_correo(db, correo_id)
    if not correo:
        return None
    for key, value in correo_data.items():
        setattr(correo, key, value)
    db.commit()
    db.refresh(correo)
    return correo
