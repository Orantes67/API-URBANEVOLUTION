from sqlalchemy.orm import Session
from app.models.seguimiento_models import Seguimiento
from app.schemas.seguimiento_schmas import SeguimientoCreate

def create_seguimiento(db: Session, seguimiento_data: SeguimientoCreate):
    db_seguimiento = Seguimiento(**seguimiento_data.dict())
    db.add(db_seguimiento)
    db.commit()
    db.refresh(db_seguimiento)
    return db_seguimiento

def get_seguimiento(db: Session, seguimiento_id: int):
    return db.query(Seguimiento).filter(Seguimiento.seguimiento_id == seguimiento_id).first()

def get_seguimientos(db: Session):
    return db.query(Seguimiento).all()

def delete_seguimiento(db: Session, seguimiento_id: int):
    seguimiento = get_seguimiento(db, seguimiento_id)
    db.delete(seguimiento)
    db.commit()
    return {"message": "Seguimiento deleted successfully"}

def update_seguimiento(db: Session, seguimiento_id: int, seguimiento_data: dict):
    seguimiento = get_seguimiento(db, seguimiento_id)
    if not seguimiento:
        return None
    for key, value in seguimiento_data.items():
        setattr(seguimiento, key, value)
    db.commit()
    db.refresh(seguimiento)
    return seguimiento
