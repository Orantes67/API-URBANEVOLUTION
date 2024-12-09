from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.comentarios_schmas import ComentariosCreate, Comentarios
from app.controllers.comentarios import (
    create_comentario,
    get_comentario,
    get_comentarios,
    delete_comentario,
    update_comentario,
)
from app.database.database import get_db

router = APIRouter()

@router.post("/", response_model=Comentarios)
def create_comentario_endpoint(comentario: ComentariosCreate, db: Session = Depends(get_db)):
    return create_comentario(db, comentario)

@router.get("/{comentario_id}", response_model=Comentarios)
def read_comentario(comentario_id: int, db: Session = Depends(get_db)):
    comentario = get_comentario(db, comentario_id)
    if comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comentario

@router.get("/", response_model=list[Comentarios])
def read_comentarios(db: Session = Depends(get_db)):
    return get_comentarios(db)

@router.put("/{comentario_id}", response_model=Comentarios)
def update_comentario_endpoint(comentario_id: int, comentario: ComentariosCreate, db: Session = Depends(get_db)):
    updated_comentario = update_comentario(db, comentario_id, comentario.dict())
    if updated_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return updated_comentario

@router.delete("/{comentario_id}")
def delete_comentario_endpoint(comentario_id: int, db: Session = Depends(get_db)):
    return delete_comentario(db, comentario_id)
