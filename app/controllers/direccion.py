from sqlalchemy.orm import Session
from app.models.direccion_models import Direccion
from app.schemas.direccion_shcmas import DireccionCreate

def create_direccion(db: Session, direccion_data: DireccionCreate):
    db_direccion = Direccion(**direccion_data.dict())
    db.add(db_direccion)
    db.commit()
    db.refresh(db_direccion)
    return db_direccion

def get_direccion(db: Session, dir_id: int):
    return db.query(Direccion).filter(Direccion.dir_id == dir_id).first()

def get_direcciones(db: Session):
    return db.query(Direccion).all()

def delete_direccion(db: Session, dir_id: int):
    direccion = get_direccion(db, dir_id)
    db.delete(direccion)
    db.commit()
    return {"message": "Direccion deleted successfully"}

def update_direccion(db: Session, dir_id: int, direccion_data: dict):
    direccion = get_direccion(db, dir_id)
    if not direccion:
        return None
    for key, value in direccion_data.items():
        setattr(direccion, key, value)
    db.commit()
    db.refresh(direccion)
    return direccion
