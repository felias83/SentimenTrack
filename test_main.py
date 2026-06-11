import os

# Configurar una URL de base de datos falsa en memoria
# ANTES de importar main.py, para que FastAPI no intente buscar a Postgres en localhost.
os.environ["DATABASE_URL"] = "sqlite:///./test_temp.db"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app  # <-- Ahora sí lo importamos de forma segura

# Configurar la base de datos SQLite real para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# --- TUS PRUEBAS UNITARIAS ---

def test_crear_comentario_positivo():
    """Verifica que la API procese un comentario positivo correctamente"""
    response = client.post(
        "/comentarios",
        json={"usuario": "Test User", "texto": "Este servicio es absolutamente fantástico y rápido."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["usuario"] == "Test User"
    assert data["sentimiento"] == "positivo"

def test_crear_comentario_negativo():
    """Verifica que la API procese un comentario negativo correctamente"""
    response = client.post(
        "/comentarios",
        json={"usuario": "Test User", "texto": "Es una porquería de sistema, se cae todo el tiempo."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentimiento"] == "negativo"