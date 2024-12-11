from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.usuarios_schmas import UsuarioCreate, Usuario,UsuarioDetalle
from app.controllers.usuario import  (
    create_usuario,
    get_usuario,
    get_usuarios,
    delete_usuario,
    update_usuario,
)
from app.database.database import get_db

router = APIRouter()

# Crear un usuario
@router.post("/", response_model=Usuario)
def create_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        # Inicia transacción
        db.begin()
        db.execute("""
            INSERT INTO usuario (nombre, apellido_p, apellido_m, edad, correo, contrasena)
            VALUES (:nombre, :apellido_p, :apellido_m, :edad, :correo, :contrasena)
        """, usuario.dict())
        db.commit()
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al crear usuario: {str(e)}")

# Obtener un usuario por ID
@router.get("/{usuario_id}", response_model=Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = get_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Obtener todos los usuarios
@router.get("/", response_model=list[Usuario])
def read_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)


@router.put("/{usuario_id}", response_model=Usuario)
def update_usuario_endpoint(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    updated_usuario = update_usuario(db, usuario_id, usuario.dict())
    if updated_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_usuario


@router.delete("/{usuario_id}")
def delete_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    return delete_usuario(db, usuario_id)

from sqlalchemy import text

@router.get("/detalles/", response_model=list[UsuarioDetalle])
def read_usuarios_detalles(db: Session = Depends(get_db)):
    query = text("""
        SELECT 
            u.usuario_id AS usuario_id,
            u.nombre AS nombre,
            u.apellido_p AS apellido_p,
            u.apellido_m AS apellido_m,
            u.edad AS edad,
            c.correo AS correo,
            p.contrasena AS contrasena
        FROM usuario u
        JOIN correo c ON u.correo_id = c.correo_id
        JOIN contrasena p ON u.contrasena_id = p.contrasena_id
    """)
    try:
        # Ejecutar consulta
        results = db.execute(query).mappings().all()

        # Validar resultados
        if not results:
            raise HTTPException(status_code=404, detail="No se encontraron usuarios con detalles")

        # Mapeo directo al esquema UsuarioDetalle
        return [UsuarioDetalle(**row) for row in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener detalles de usuarios: {str(e)}")