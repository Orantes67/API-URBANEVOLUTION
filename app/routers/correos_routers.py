from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.correos_schmas import CorreoCreate, Correo
from app.controllers.correos import (
    create_correo,
    get_correo,
    get_correos,
    delete_correo,
    update_correo,
)
from app.database.database import get_db

router = APIRouter()

# Crear un correo
@router.post("/", response_model=Correo)
def create_correo_endpoint(correo: CorreoCreate, db: Session = Depends(get_db)):
    return create_correo(db, correo)

# Obtener un correo por ID
@router.get("/{correo_id}", response_model=Correo)
def read_correo(correo_id: int, db: Session = Depends(get_db)):
    correo = get_correo(db, correo_id)
    if correo is None:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    return correo

# Obtener todos los correos
@router.get("/", response_model=list[Correo])
def read_correos(db: Session = Depends(get_db)):
    return get_correos(db)

# Actualizar un correo
@router.put("/{correo_id}", response_model=Correo)
def update_correo_endpoint(correo_id: int, correo: CorreoCreate, db: Session = Depends(get_db)):
    updated_correo = update_correo(db, correo_id, correo.dict())
    if updated_correo is None:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    return updated_correo

# Eliminar un correo
@router.delete("/{correo_id}")
def delete_correo_endpoint(correo_id: int, db: Session = Depends(get_db)):
    return delete_correo(db, correo_id)
