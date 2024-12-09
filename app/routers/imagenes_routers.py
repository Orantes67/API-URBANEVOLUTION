from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.schemas.imagenes_schmas import ImagenesCreate, Imagenes  # Correcto
from app.controllers.imagenes import (
    create_imagen,
    get_imagen,
    get_imagenes,
    delete_imagen,
    update_imagen,
)
from app.database.database import get_db
import os
from fastapi.responses import FileResponse

router = APIRouter()

# Crear una imagen (subir una imagen)
@router.post("/", response_model=Imagenes)  # Respuesta con el esquema Imagenes
async def create_imagen_endpoint(imagen: ImagenesCreate, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Guardar el archivo en el sistema de archivos
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    return create_imagen(db, imagen, file_location)

# Obtener una imagen por ID
@router.get("/{imagen_id}", response_model=Imagenes)
def read_imagen(imagen_id: int, db: Session = Depends(get_db)):
    imagen = get_imagen(db, imagen_id)
    if imagen is None:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    return imagen

# Obtener todas las imágenes
@router.get("/", response_model=list[Imagenes])
def read_imagenes(db: Session = Depends(get_db)):
    return get_imagenes(db)

# Actualizar una imagen
@router.put("/{imagen_id}", response_model=Imagenes)
async def update_imagen_endpoint(imagen_id: int, imagen: ImagenesCreate, file: UploadFile = File(None), db: Session = Depends(get_db)):
    updated_imagen = update_imagen(db, imagen_id, imagen.dict())
    if updated_imagen is None:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

    if file:
        # Eliminar la imagen anterior
        os.remove(updated_imagen.file_path)
        
        # Guardar el nuevo archivo
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        updated_imagen.file_path = file_location
        db.commit()

    return updated_imagen

# Eliminar una imagen
@router.delete("/{imagen_id}")
def delete_imagen_endpoint(imagen_id: int, db: Session = Depends(get_db)):
    imagen = delete_imagen(db, imagen_id)
    if imagen is None:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    
    # Eliminar el archivo físico
    os.remove(imagen.file_path)
    
    return {"detail": "Imagen eliminada"}

# Obtener imagen como archivo
@router.get("/file/{filename}")
async def get_imagen_file(filename: str):
    file_path = f"uploads/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    return FileResponse(file_path)
