import os
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# Configuración de la página web
st.set_page_config(page_title="SentimenTrack AI Dashboard", page_icon="📈", layout="wide")

st.title("📈 SentimenTrack AI - Panel de Reputación de Marca")
st.markdown("Monitoreo de comentarios y análisis de sentimiento con Inteligencia Artificial en tiempo real.")

# 1. Intenta leer la URL desde las variables de entorno de Docker.
# 2. Si no existe (Plan B: fuera de Docker), usa localhost por defecto.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/comentarios")

# 🔥 TRUCO MÁGICO: Crear un contenedor vacío que limpiaremos y redibujaremos
placeholder = st.empty()

# Bucle infinito para simular el tiempo real
while True:
    with placeholder.container():    
        # --- OBTENER DATOS DE LA API ---
        try:
            respuesta = requests.get(API_URL)
            datos = respuesta.json()
            
            if datos:
                # Convertimos los datos JSON de la API en un DataFrame de Pandas (tabla)
                df = pd.DataFrame(datos)
                
                # --- SECCIÓN 1: MÉTRICAS CLAVE ---
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total de Comentarios", len(df))
                with col2:
                    positivos = len(df[df['sentimiento'] == 'positivo'])
                    st.metric("😊 Positivos", positivos)
                with col3:
                    negativos = len(df[df['sentimiento'] == 'negativo'])
                    # Mostramos una alerta si hay comentarios negativos
                    st.metric("😡 Negativos", negativos, delta=f"{negativos} alertas críticas" if negativos > 0 else "Limpio")

                st.markdown("---")

                # --- SECCIÓN 2: GRÁFICOS INTERACTIVOS ---
                col_izq, col_der = st.columns(2)
                
                with col_izq:
                    st.subheader("📊 Distribución de Sentimientos")
                    # Conteo de sentimientos para el gráfico de pastel
                    conteo = df['sentimiento'].value_counts().reset_index()
                    conteo.columns = ['Sentimiento', 'Cantidad']
                    fig_pastel = px.pie(conteo, values='Cantidad', names='Sentimiento', 
                                        color='Sentimiento',
                                        color_discrete_map={'positivo': '#2ecc71', 'neutral': '#f1c40f', 'negativo': '#e74c3c'})
                    st.plotly_chart(fig_pastel, use_container_width=True, key=f"pastel_{time.time()}")

                with col_der:
                    st.subheader("📋 Últimos Comentarios Procesados")
                    # Mostramos los comentarios en una tabla limpia, ordenados por los más recientes
                    df_mostrar = df[['usuario', 'texto', 'sentimiento', 'confianza']].iloc[::-1]
                    st.dataframe(df_mostrar, use_container_width=True, key=f"tabla_{time.time()}")

            else:
                st.info("Aún no hay comentarios guardados en la base de datos. Ve a la documentación de la API para agregar algunos.")

        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")
            
    # ⏱️ Pausa el dashboard por 3 segundos antes de volver a leer la base de datos
    time.sleep(3)