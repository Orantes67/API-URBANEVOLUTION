from sqlalchemy.orm import Session
from app.models.comentarios_models import Comentarios
from app.schemas.comentarios_schmas import ComentariosCreate  # Corregir importación

def create_comentario(db: Session, comentario_data: ComentariosCreate):
    db_comentario = Comentarios(**comentario_data.dict())  # Usar .dict() para convertir los datos a un formato adecuado para SQLAlchemy
    db.add(db_comentario)
    db.commit()
    db.refresh(db_comentario)
    return db_comentario

def get_comentario(db: Session, comentarios_id: int):
    return db.query(Comentarios).filter(Comentarios.comentarios_id == comentarios_id).first()

def get_comentarios(db: Session):
    return db.query(Comentarios).all()

def delete_comentario(db: Session, comentarios_id: int):
    comentario = get_comentario(db, comentarios_id)
    db.delete(comentario)
    db.commit()
    return {"message": "Comentario deleted successfully"}

def update_comentario(db: Session, comentarios_id: int, comentario_data: dict):
    comentario = get_comentario(db, comentarios_id)
    if not comentario:
        return None
    for key, value in comentario_data.items():
        setattr(comentario, key, value)
    db.commit()
    db.refresh(comentario)
    return comentario
