import os
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Importamos la librería para leer el archivo .env local
from dotenv import load_dotenv

# Carga las variables del archivo .env si existe (esto se activa fuera de Docker)
load_dotenv()

# 1. Intentamos leer la URL completa que inyecta Docker.
# 2. Si no existe (Plan B: local fuera de Docker), la armamos dinámicamente usando las variables locales del .env
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}"
)

# El 'engine' es el encargado de comunicarse con Docker
engine = create_engine(DATABASE_URL)

# Creamos una sesión para hacer consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esta clase base la usaremos para crear nuestras tablas (Modelos)
Base = sqlalchemy.orm.declarative_base()

# Función auxiliar para abrir y cerrar la conexión automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()