SentimenTrack AI 🚀
SentimenTrack AI es un ecosistema completo de microservicios diseñado para la ingesta, procesamiento analítico y visualización en tiempo real de comentarios de usuarios. El sistema utiliza Inteligencia Artificial (Modelos NLP de Hugging Face) para clasificar automáticamente el sentimiento de los textos ingresados.

La arquitectura está completamente contenerizada, es escalable, segura y cuenta con un pipeline automatizado de calidad de código.

🏗️ Arquitectura del Sistema
El proyecto está compuesto por 4 microservicios independientes que se comunican de forma asíncrona dentro de una red aislada de Docker:

Backend API (FastAPI): Núcleo del sistema. Expone endpoints REST, integra el modelo de IA y gestiona la lógica de negocio.

Base de Datos (PostgreSQL): Almacenamiento relacional persistente para los usuarios, comentarios y resultados analíticos.

Data Ingestor (Simulador Continuo): Un productor de datos automatizado que genera ráfagas constantes de tráfico simulando un entorno de producción real.

Dashboard (Streamlit & Plotly): Interfaz gráfica interactiva que consume los datos procesados para mostrar métricas clave, gráficos de barras y líneas de tiempo en vivo.

⚡ Funcionalidades Clave
📥 Ingesta de Datos en Simulación Continuo (Data Ingestion)
Se incorporó un servicio autónomo (ingestador.py) que actúa como un flujo continuo de datos de entrada. Este componente genera comentarios realistas con diversas cargas emocionales y los envía mediante peticiones POST a la API en intervalos aleatorios de 2 a 5 segundos, manteniendo el ecosistema dinámico y simulando un entorno con tráfico real.

🧪 Suite de Pruebas Unitarias (Testing)
Se diseñó una arquitectura de pruebas utilizando pytest y httpx. Para garantizar la integridad de la base de datos de producción, los tests levantan una base de datos SQLite en memoria de forma efímera, aislando completamente el entorno de ejecución de pruebas y validando los códigos de respuesta (200 OK) y la precisión de las etiquetas de la IA.

🔄 Integración Continua (CI con GitHub Actions)
Se implementó un pipeline de DevOps en la nube que se dispara automáticamente con cada git push o pull_request hacia la rama main. El flujo de trabajo levanta un entorno virtual Linux (Ubuntu), configura el entorno bajo Node.js 24 y Python 3.12 de forma segura, instala dependencias y ejecuta la suite de tests automatizada.

🛠️ Stack Tecnológico
Backend: Python 3.12, FastAPI, SQLAlchemy, Uvicorn.

IA/NLP: Hugging Face (Modelos de Análisis de Sentimiento).

Database: PostgreSQL 15 / SQLite (para entornos de pruebas).

Frontend/Analytics: Streamlit, Plotly.

DevOps & CI/CD: Docker, Docker Compose, GitHub Actions.

🚀 Instalación y Despliegue Rápido (Local)
Gracias a la contenerización global, puedes poner a correr todo el ecosistema (incluyendo el simulador continuo de datos) con un único comando.

Prerrequisitos
Tener instalado Docker y Docker Compose.

Instrucciones
Paso 1: Clona este repositorio

git clone https://github.com/TU_USUARIO/SentimenTrack.git

cd SentimenTrack

Paso 2: Configura tus variables de entorno
Crea un archivo llamado .env en la raíz del proyecto y agrega exactamente la siguiente línea de código para conectar la base de datos de Docker de forma segura:

DATABASE_URL=postgresql://postgres:postgres@db:5432/sentimentrack

Paso 3: Despliega la arquitectura completa
Ejecuta el siguiente comando en tu terminal para compilar las imágenes locales (api, dashboard, ingestador) e iniciar el flujo de datos:

docker compose up --build

🎯 Puertos Locales Disponibles:
Una vez que Docker termine de levantar los contenedores, puedes acceder a los servicios desde tu navegador:

API de FastAPI (Documentación Swagger): http://localhost:8000/docs

Dashboard Analítico en Vivo (Streamlit): http://localhost:8501

🔬 Ejecución de Tests en Local
Si deseas correr la suite de pruebas unitarias de forma aislada en tu entorno virtual local sin encender Docker, ejecuta en tu terminal:

Instalar dependencias: pip install -r requirements.txt pytest httpx

Ejecutar los tests: pytest -v