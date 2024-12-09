from sqlalchemy.orm import Session
from app.models.usuario_models import Usuario
from app.schemas.usuarios_schmas import UsuarioCreate

def create_usuario(db: Session, usuario_data: UsuarioCreate):
    db_usuario = Usuario(**usuario_data.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def delete_usuario(db: Session, usuario_id: int):
    usuario = get_usuario(db, usuario_id)
    db.delete(usuario)
    db.commit()
    return {"message": "Usuario deleted successfully"}

def update_usuario(db: Session, usuario_id: int, usuario_data: dict):
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        return None
    for key, value in usuario_data.items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario
