from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.direccion_shcmas import DireccionCreate, Direccion
from app.controllers.direccion import (
    create_direccion,
    get_direccion,
    get_direcciones,
    delete_direccion,
    update_direccion,
)
from app.database.database import get_db

router = APIRouter()

# Crear una dirección
@router.post("/", response_model=Direccion)
def create_direccion_endpoint(direccion: DireccionCreate, db: Session = Depends(get_db)):
    return create_direccion(db, direccion)

# Obtener una dirección por ID
@router.get("/{direccion_id}", response_model=Direccion)
def read_direccion(direccion_id: int, db: Session = Depends(get_db)):
    direccion = get_direccion(db, direccion_id)
    if direccion is None:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return direccion

# Obtener todas las direcciones
@router.get("/", response_model=list[Direccion])
def read_direcciones(db: Session = Depends(get_db)):
    return get_direcciones(db)

# Actualizar una dirección
@router.put("/{direccion_id}", response_model=Direccion)
def update_direccion_endpoint(direccion_id: int, direccion: DireccionCreate, db: Session = Depends(get_db)):
    updated_direccion = update_direccion(db, direccion_id, direccion.dict())
    if updated_direccion is None:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return updated_direccion

# Eliminar una dirección
@router.delete("/{direccion_id}")
def delete_direccion_endpoint(direccion_id: int, db: Session = Depends(get_db)):
    return delete_direccion(db, direccion_id)
