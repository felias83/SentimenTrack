#!/bin/bash

echo "🚀 Iniciando el entorno de SentimenTrack AI..."

# 1. Levantar la base de datos en Docker en segundo plano
echo "🐳 Verificando base de datos en Docker..."
docker compose up -d

# 2. Activar el entorno virtual de Python
echo "🐍 Activando entorno virtual..."
source venv/bin/activate

# 3. Lanzar la API de FastAPI en segundo plano
echo "🔥 Arrancando API (FastAPI) en el puerto 8000..."
uvicorn main:app --host 127.0.0.1 --port 8000 &

# Esperar 3 segundos a que la API levante bien
sleep 3

# 4. Lanzar el Dashboard de Streamlit
echo "📊 Abriendo el Dashboard de Streamlit..."
streamlit run dashboard.py