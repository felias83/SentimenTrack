from transformers import pipeline

print("🤖 Cargando modelo de Inteligencia Artificial... (Esto solo ocurre una vez)")

# Cargamos un modelo pre-entrenado en español específico para análisis de sentimiento
# Usamos la canalización 'sentiment-analysis' que facilita todo el trabajo
analizador = pipeline(
    "sentiment-analysis", 
    model="pysentimiento/robertuito-sentiment-analysis"
)

def analizar_texto_ia(texto: str):
    """
    Recibe un texto, lo pasa por el modelo de IA y devuelve
    el sentimiento (POS, NEG, NEU) y el porcentaje de confianza.
    """
    try:
        resultado = analizador(texto)[0]
        
        # Mapeamos las etiquetas del modelo a nombres más amigables
        etiquetas = {
            "POS": "positivo",
            "NEG": "negativo",
            "NEU": "neutral"
        }
        
        sentimiento_final = etiquetas.get(resultado['label'], "neutral")
        confianza_final = round(resultado['score'], 2) # Redondeamos a 2 decimales
        
        return sentimiento_final, confianza_final
    except Exception as e:
        print(f"❌ Error al procesar con IA: {e}")
        # En caso de error, devolvemos un valor por defecto para que la app no se caiga
        return "neutral", 0.0