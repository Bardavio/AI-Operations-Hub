# AI Operations Hub (Tessera Business Automation) 🛠️

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

## 🛠️ Instalación y Uso Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Bardavio/AI-Operations-Hub.git
cd AI-Operations-Hub
```

### Método A: Ejecución con Docker (Recomendado y más rápido) 🐳
Dado que la aplicación está completamente contenerizada, no necesitas configurar Python ni instalar dependencias directamente en tu sistema.

1. **Configurar las API Keys:**
   Abre el archivo `.env` en la raíz del proyecto e introduce tu OpenAI API Key:
   ```bash
   OPENAI_API_KEY=tu_clave_de_openai_aqui
   ```
2. **Levantar la aplicación:**
   Ejecuta en tu terminal el siguiente comando:
   ```bash
   docker compose up --build -d
   ```
3. **Acceder a la aplicación:**
   Abre tu navegador y entra en: **`http://localhost:8501`**

---

### Método B: Ejecución en Local (Sin Docker) 🐍
Si prefieres ejecutarlo de forma nativa en tu entorno de Python:

1. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar las API Keys:**
   Crea tu archivo `.env` o introduce la clave de OpenAI directamente en la interfaz gráfica de la aplicación una vez levantada.
4. **Lanzar la aplicación:**
   ```bash
   streamlit run app.py
   ```

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
