# Tessera AI Automation Hub 🛠️

Este repositorio contiene una demostración práctica de dos herramientas de **Inteligencia Artificial y Automatización** desarrolladas específicamente para resolver cuellos de botella reales en empresas de consultoría estratégica y de talento como **Tessera**.

Este proyecto ha sido diseñado para demostrar el valor diferencial de mi perfil híbrido: **Doble Grado en Ingeniería Informática y ADE** (Administración y Dirección de Empresas).

---

## 🏗️ Arquitectura y Proyectos Incluidos

La aplicación se compone de un portal web interactivo desarrollado con **Streamlit** en **Python**, estructurado en dos módulos clave:

### 1. 📄 Evaluador Inteligente de CVs (AI Resume Screener)
Una herramienta diseñada para optimizar los procesos de selección y reclutamiento (área clave de talento en Tessera):
* **Cribado Semántico:** Lector de archivos PDF que procesa el texto del currículum y lo compara de manera conceptual con los requisitos de la vacante.
* **Salida Estructurada (JSON/Pydantic):** A través de LangChain, forzamos al modelo (GPT-4o-mini) a devolver un análisis riguroso y tipado con:
  * Porcentaje de ajuste del candidato.
  * 3 puntos fuertes principales del perfil.
  * 3 lagunas o carencias frente al puesto.
* **Guion de Entrevista Personalizado:** Genera automáticamente 3 preguntas complejas diseñadas específicamente para indagar en las debilidades del candidato en la entrevista técnica.

### 2. 🔍 Investigador y Redactor Comercial (Client Research & Outreach Agent)
Una herramienta diseñada para prospección comercial de nuevos clientes y preparación de reuniones de consultoría de crecimiento:
* **Búsqueda Web en Tiempo Real:** El usuario introduce el nombre de la empresa y la IA realiza búsquedas en la web (usando la herramienta de búsqueda de DuckDuckGo o Tavily API) para encontrar proyectos recientes, cultura corporativa y noticias.
* **Propuesta Personalizada por Email:** Utilizando la información fresca recuperada de internet, la IA redacta un correo en frío para un directivo de la empresa objetivo, alineando los servicios de Tessera con la situación actual de su negocio.

---

## 🧠 ¿Por qué este proyecto demuestra el Perfil Informática + ADE?

* **La Capa de Tecnología (Informática):**
  * Uso de **Python** y **Streamlit** para crear una UI fluida y profesional.
  * Orquestación de LLMs con **LangChain** (estructuración de prompts, cadenas y control de temperaturas).
  * Extracción de datos en tiempo real mediante web scraping/search en LangChain.
  * **Structured Outputs** mediante modelos de datos en Pydantic.
* **La Capa de Negocio (ADE):**
  * Enfoque directo en la optimización de procesos (reducción de tiempos de selección y prospección comercial).
  * Redacción comercial persuasiva alineada con necesidades reales de crecimiento corporativo.
  * Comprensión de los cuellos de botella en RRHH y Desarrollo de Negocio.

---

## 🛠️ Instalación y Uso Local

Sigue estos sencillos pasos para probar la aplicación en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tessera-ai-automation.git
cd tessera-ai-automation
```

### 2. Instalar las dependencias
Se recomienda utilizar un entorno virtual (venv):
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar las API Keys
Duplica el archivo `.env.example`, renombralo como `.env` e introduce tus claves de API de OpenAI:
```bash
OPENAI_API_KEY=tu_clave_de_openai
# Opcional: TAVILY_API_KEY=tu_clave_de_tavily
```
*Nota: Si prefieres no usar el archivo `.env`, puedes introducir tu **OpenAI API Key** directamente en la barra lateral de la aplicación web una vez levantada.*

### 4. Lanzar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado (normalmente en `http://localhost:8501`).

---

## ⚙️ Tecnologías Utilizadas

* **Python 3.11**
* **Streamlit** (Interfaz de usuario)
* **LangChain** (Orquestación del LLM y herramientas de búsqueda)
* **OpenAI API (GPT-4o-mini)**
* **PyPDF2** (Lector y parser de currículums en PDF)
* **Tavily / DuckDuckGo Search** (Motores de búsqueda para recopilación de información)

---

**Desarrollado por Sergio Bardavio** - [LinkedIn](https://www.linkedin.com/in/tu-perfil/) | [GitHub](https://github.com/tu-usuario/)
