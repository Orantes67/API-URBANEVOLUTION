from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.seguimiento_schmas import SeguimientoCreate, Seguimiento
from app.controllers.seguimiento import (
    create_seguimiento,
    get_seguimiento,
    get_seguimientos,
    delete_seguimiento,
    update_seguimiento,
)
from app.database.database import get_db

router = APIRouter()

# Crear un seguimiento
@router.post("/", response_model=Seguimiento)
def create_seguimiento_endpoint(seguimiento: SeguimientoCreate, db: Session = Depends(get_db)):
    return create_seguimiento(db, seguimiento)

# Obtener un seguimiento por ID
@router.get("/{seguimiento_id}", response_model=Seguimiento)
def read_seguimiento(seguimiento_id: int, db: Session = Depends(get_db)):
    seguimiento = get_seguimiento(db, seguimiento_id)
    if seguimiento is None:
        raise HTTPException(status_code=404, detail="Seguimiento not found")
    return seguimiento

# Obtener todos los seguimientos
@router.get("/", response_model=list[Seguimiento])
def read_seguimientos(db: Session = Depends(get_db)):
    return get_seguimientos(db)

# Actualizar un seguimiento
@router.put("/{seguimiento_id}", response_model=Seguimiento)
def update_seguimiento_endpoint(seguimiento_id: int, seguimiento: SeguimientoCreate, db: Session = Depends(get_db)):
    updated_seguimiento = update_seguimiento(db, seguimiento_id, seguimiento.dict())
    if updated_seguimiento is None:
        raise HTTPException(status_code=404, detail="Seguimiento not found")
    return updated_seguimiento

# Eliminar un seguimiento
@router.delete("/{seguimiento_id}")
def delete_seguimiento_endpoint(seguimiento_id: int, db: Session = Depends(get_db)):
    return delete_seguimiento(db, seguimiento_id)
