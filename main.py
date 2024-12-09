from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.routers import (
    usuario_routers,comentarios_routers,direccion_routers,imagenes_routers,post_routers,seguimiento_routers,contraseña_routers,correos_routers
)
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Inicializa la aplicación FastAPI
app = FastAPI()

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" a una lista específica de dominios si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creación de tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registro de los routers
app.include_router(usuario_routers.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(comentarios_routers.router, prefix="/comentarios", tags=["Comentarios"])
app.include_router(direccion_routers.router, prefix="/direcciones", tags=["Direcciones"])
app.include_router(imagenes_routers.router, prefix="/imagenes", tags=["Imágenes"])
app.include_router(post_routers.router, prefix="/posts", tags=["Posts"])
app.include_router(seguimiento_routers.router, prefix="/seguimientos", tags=["Seguimientos"])
app.include_router(correos_routers.router, prefix="/correos",tags=["Correos"])
# Endpoint de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}
