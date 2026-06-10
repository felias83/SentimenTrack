from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db
# 1. Importamos nuestra función de IA
from analyzer import analizar_texto_ia 

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SentimenTrack AI API", version="1.0")

class ComentarioCreate(BaseModel):
    usuario: str
    texto: str

@app.get("/")
def inicio():
    return {"mensaje": "SentimenTrack AI funcionando con IA y conectado a PostgreSQL"}

# 2. Modificamos el endpoint para usar IA real
@app.post("/comentarios")
def crear_comentario(comentario: ComentarioCreate, db: Session = Depends(get_db)):
    
    # 🔥 AQUÍ OCURRE LA MAGIA: Pasamos el texto por la IA real
    sentimiento_ia, confianza_ia = analizar_texto_ia(comentario.texto)
    
    # Guardamos el resultado real en la base de datos de Docker
    nuevo_comentario = models.Comentario(
        usuario=comentario.usuario,
        texto=comentario.texto,
        sentimiento=sentimiento_ia,
        confianza=confianza_ia
    )
    
    db.add(nuevo_comentario)
    db.commit()
    db.refresh(nuevo_comentario)
    return nuevo_comentario

@app.get("/comentarios")
def listar_comentarios(db: Session = Depends(get_db)):
    return db.query(models.Comentario).all()