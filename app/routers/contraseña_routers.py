from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.contraseña_schmas import ContrasenaCreate, Contrasena
from app.controllers.contraseña import (
    create_contrasena,
    get_contrasena,
    get_contrasenas,
    delete_contrasena,
    update_contrasena,
)
from app.database.database import get_db

router = APIRouter()

# Crear una contraseña
@router.post("/", response_model=Contrasena)
def create_contrasena_endpoint(contrasena: ContrasenaCreate, db: Session = Depends(get_db)):
    return create_contrasena(db, contrasena)

# Obtener una contraseña por ID
@router.get("/{contrasena_id}", response_model=Contrasena)
def read_contrasena(contrasena_id: int, db: Session = Depends(get_db)):
    contrasena = get_contrasena(db, contrasena_id)
    if contrasena is None:
        raise HTTPException(status_code=404, detail="Contrasena not found")
    return contrasena

# Obtener todas las contraseñas
@router.get("/", response_model=list[Contrasena])
def read_contrasenas(db: Session = Depends(get_db)):
    return get_contrasenas(db)

# Actualizar una contraseña
@router.put("/{contrasena_id}", response_model=Contrasena)
def update_contrasena_endpoint(contrasena_id: int, contrasena: ContrasenaCreate, db: Session = Depends(get_db)):
    updated_contrasena = update_contrasena(db, contrasena_id, contrasena.dict())
    if updated_contrasena is None:
        raise HTTPException(status_code=404, detail="Contrasena not found")
    return updated_contrasena

# Eliminar una contraseña
@router.delete("/{contrasena_id}")
def delete_contrasena_endpoint(contrasena_id: int, db: Session = Depends(get_db)):
    return delete_contrasena(db, contrasena_id)
