# 📈 SentimenTrack AI - Panel de Reputación de Marca en Tiempo Real

SentimenTrack AI es una aplicación de grado de producción basada en una **arquitectura de microservicios**. El sistema captura comentarios de usuarios, procesa su contenido mediante un modelo de **Inteligencia Artificial** de Procesamiento de Lenguaje Natural (NLP) para determinar el sentimiento (positivo/negativo) y despliega métricas analíticas en tiempo real en un panel interactivo.

## 🛠️ Tecnologías Utilizadas

* **Backend:** FastAPI (Python), Uvicorn.
* **Inteligencia Artificial:** Hugging Face (Transformers - Sentiment Analysis).
* **Base de Datos:** PostgreSQL, SQLAlchemy (ORM).
* **Frontend:** Streamlit, Plotly (Gráficos interactivos).
* **DevOps & Seguridad:** Docker, Docker Compose, Variables de Entorno (`.env`).

## 🚀 Arquitectura del Sistema

El proyecto está completamente contenerizado en **Docker**, dividiéndose en 3 microservicios independientes que se comunican de forma aislada dentro de una red privada de Docker Compose:
1.  `sentimentrack_db`: Base de datos relacional robusta.
2.  `sentimentrack_api`: Capa backend que expone endpoints REST e integra el pipeline de IA.
3.  `sentimentrack_dashboard`: Interfaz web que consume la API y procesa métricas analíticas.

## ⚙️ Instrucciones de Instalación y Despliegue

### Requisitos Previos
* Docker y Docker Compose instalados.

### Pasos para Ejecutar
1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/TU_USUARIO/SentimenTrack.git](https://github.com/TU_USUARIO/SentimenTrack.git)
    cd SentimenTrack
    ```
2.  Crea un archivo `.env` en la raíz del proyecto basándote en las variables requeridas (el archivo `.env` está protegido en `.gitignore` por buenas prácticas de seguridad de DevSecOps):
    ```text
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña_segura
    DB_NAME=sentimentrack
    ```
3.  Construye y enciende todo el ecosistema con un solo comando:
    ```bash
    docker compose up --build
    ```

### 📊 Acceso a los Servicios
* **Dashboard Visual (Frontend):** Accede a `http://localhost:8501`
* **Documentación Interactiva (API / Swagger):** Accede a `http://localhost:8000/docs`