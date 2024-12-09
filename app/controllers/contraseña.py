from sqlalchemy.orm import Session
from app.models.contraseña_models import Contrasena
from app.schemas.contraseña_schmas import ContrasenaCreate

def create_contrasena(db: Session, contrasena_data: ContrasenaCreate):
    db_contrasena = Contrasena(**contrasena_data.dict())
    db.add(db_contrasena)
    db.commit()
    db.refresh(db_contrasena)
    return db_contrasena

def get_contrasena(db: Session, contrasena_id: int):
    return db.query(Contrasena).filter(Contrasena.contrasena_id == contrasena_id).first()

def get_contrasenas(db: Session):
    return db.query(Contrasena).all()

def delete_contrasena(db: Session, contrasena_id: int):
    contrasena = get_contrasena(db, contrasena_id)
    db.delete(contrasena)
    db.commit()
    return {"message": "Contrasena deleted successfully"}

def update_contrasena(db: Session, contrasena_id: int, contrasena_data: dict):
    contrasena = get_contrasena(db, contrasena_id)
    if not contrasena:
        return None
    for key, value in contrasena_data.items():
        setattr(contrasena, key, value)
    db.commit()
    db.refresh(contrasena)
    return contrasena
