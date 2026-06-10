import time
import random
import requests

API_URL = "http://api:8000/comentarios"

# Banco de datos para simular clientes reales
USUARIOS = ["Andrés F.", "Camila R.", "John Doe", "María F.", "Lucas M.", "Sonia T.", "Roberto V."]

COMENTARIOS_POSITIVOS = [
    "Me encanta la nueva actualización, va súper fluida.",
    "El soporte técnico me resolvió el problema en cinco minutos, excelente.",
    "Es la mejor aplicación de tracking que he usado en años.",
    "El diseño de la interfaz es hermoso y muy intuitivo."
]

COMENTARIOS_NEGATIVOS = [
    "Qué desastre de aplicación, se cierra sola cada vez que intento abrir el menú.",
    "El servicio es pésimo, llevo tres días esperando una respuesta de soporte.",
    "Es demasiado lenta al cargar los datos, no la recomiendo para nada.",
    "Me cobraron dos veces la suscripción y nadie me da una solución."
]

print("🚀 Iniciando Simulador de Ingesta Continua...")

while True:
    try:
        # Decidir aleatoriamente si el comentario será positivo o negativo
        tipo = random.choice(["positivo", "negativo"])
        texto = random.choice(COMENTARIOS_POSITIVOS if tipo == "positivo" else COMENTARIOS_NEGATIVOS)
        usuario = random.choice(USUARIOS)
        
        payload = {"usuario": usuario, "texto": texto}
        
        # Enviar el comentario a la API de FastAPI dentro de Docker
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            print(f"📥 Ingestado con éxito | Usuario: {usuario} | Sentimiento simulado: {tipo}")
        else:
            print(f"⚠️ Error en la API: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error de conexión con la API: {e}")
    
    # Esperar un tiempo aleatorio entre 2 y 5 segundos antes de enviar el siguiente
    time.sleep(random.uniform(2.0, 5.0))