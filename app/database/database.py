from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de la base de datos
SQLALCHEMY_DATABASE_URL = (
    #"postgresql+psycopg2://hector:tu_contraseña_fuerte@44.206.97.188:5432/urbanevolution"
    "postgresql+psycopg2://hector:@localhost:5432/UrbanEvolution"
)

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos
Base = declarative_base()


def get_db():
    """
    Función para obtener una sesión de la base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
