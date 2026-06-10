from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    
    # Estos campos los llenará la IA más adelante
    sentimiento = Column(String, nullable=True) # "positivo", "negativo", "neutral"
    confianza = Column(Float, nullable=True)     # Ej: 0.94 (94% de seguridad)
    
    # Fecha de creación automática
    fecha_creacion = Column(DateTime, default=datetime.now)