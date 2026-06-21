import streamlit as st
import pypdf
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.tools import DuckDuckGoSearchRun
from pydantic import BaseModel, Field
from typing import List

# Cargar variables de entorno locales si existen (.env)
load_dotenv()

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Tessera AI Automation Hub",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para una estética premium
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF4B4B, #1A73E8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #5f6368;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 3rem;
        font-weight: 800;
        color: #1A73E8;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: Configuración y API Keys ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/000000/artificial-intelligence.png", width=100)
    st.markdown("### Tessera AI Automation Hub 🛠️")
    st.markdown("---")
    
    st.markdown("#### 🔑 Configuración de API")
    # Obtener API keys desde variables de entorno o input del usuario
    env_openai_key = os.getenv("OPENAI_API_KEY", "")
    openai_key = st.text_input(
        "OpenAI API Key",
        value=env_openai_key,
        type="password",
        help="Introduce tu clave de API de OpenAI para activar las funcionalidades de IA."
    )
    
    env_tavily_key = os.getenv("TAVILY_API_KEY", "")
    tavily_key = st.text_input(
        "Tavily API Key (Opcional)",
        value=env_tavily_key,
        type="password",
        help="Opcional. Si se proporciona, se usará Tavily para búsquedas más precisas. Si no, usaremos DuckDuckGo (gratis)."
    )

    st.markdown("---")
    st.markdown("#### 👤 Perfil del Candidato")
    st.info("""
    **Sergio Bardavio**
    *Estudiante Doble Grado:*
    Ingeniería Informática + ADE
    *Especialidad:* Automatización, IA y Cloud.
    """)

# Mensaje de advertencia si no hay API Key de OpenAI
if not openai_key:
    st.warning("⚠️ Introduce tu **OpenAI API Key** en la barra lateral para comenzar a utilizar la aplicación.")
    st.stop()

# Inicializar el modelo de OpenAI
llm = ChatOpenAI(api_key=openai_key, model="gpt-4o-mini", temperature=0.2)

# --- DEFINICIÓN DE CLASES PYDANTIC PARA SALIDA ESTRUCTURADA ---
class CandidateEvaluation(BaseModel):
    match_score: int = Field(description="Puntuación de ajuste de 0 a 100 basado en la experiencia y requisitos de la oferta.")
    strengths: List[str] = Field(description="Lista de exactamente 3 puntos fuertes del candidato relevantes para la oferta.")
    gaps: List[str] = Field(description="Lista de exactamente 3 carencias o áreas de mejora del candidato frente a la oferta.")
    interview_questions: List[str] = Field(description="Lista de exactamente 3 preguntas de entrevista personalizadas y técnicas basadas en las lagunas de su perfil.")
    summary: str = Field(description="Un resumen ejecutivo de 3 oraciones sobre el encaje y recomendación final de contratación.")

# --- FUNCIONES AUXILIARES ---
def extract_text_from_pdf(file):
    """Extrae el texto de un archivo PDF subido a Streamlit."""
    try:
        pdf_reader = pypdf.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"Error al leer el PDF: {e}")
        return ""

def search_company_info(company_name, company_website, tavily_api_key):
    """Realiza una búsqueda de información sobre la empresa objetivo en internet."""
    query = f"{company_name} {company_website} noticias recientes proyectos tecnología automatización"
    
    if tavily_api_key:
        try:
            from tavily import TavilyClient
            client = TavilyClient(api_key=tavily_api_key)
            response = client.search(query=query, max_results=3)
            search_text = ""
            for result in response.get('results', []):
                search_text += f"Título: {result.get('title')}\nContenido: {result.get('content')}\nURL: {result.get('url')}\n\n"
            return search_text, "Tavily"
        except Exception as e:
            st.warning(f"Error al usar Tavily, usando DuckDuckGo como alternativa: {e}")
            
    # Fallback o por defecto: DuckDuckGo
    try:
        search = DuckDuckGoSearchRun()
        return search.run(query), "DuckDuckGo (Gratuito)"
    except Exception as e:
        return f"No se pudo realizar la búsqueda automatizada. Procediendo con el conocimiento base del modelo. (Detalle: {e})", "Ninguno (Conocimiento Base)"

# --- DISEÑO PRINCIPAL (TABS) ---
st.markdown("<h1 class='main-title'>Tessera AI Automation Hub</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Demostración de automatizaciones de negocio e IA para consultoría estratégica y de talento.</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📄 Evaluador Inteligente de CVs", "🔍 Investigador y Redactor Comercial"])

# ==========================================
# TAB 1: EVALUADOR INTELIGENTE DE CVs
# ==========================================
with tab1:
    st.header("📄 Cribado Automatizado y Planificador de Entrevistas")
    st.write("Sube el currículum de un candidato y pega los detalles de la vacante para obtener un análisis semántico instantáneo y un guion de entrevista a medida.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Subir Currículum (PDF)")
        cv_file = st.file_uploader("Sube el CV en formato PDF", type=["pdf"])
        
        cv_text = ""
        if cv_file is not None:
            cv_text = extract_text_from_pdf(cv_file)
            st.success("✅ Currículum subido y procesado correctamente.")
            with st.expander("Ver texto extraído del CV"):
                st.text(cv_text[:1000] + "...")
                
    with col2:
        st.subheader("2. Detalles de la Oferta de Empleo")
        job_description = st.text_area(
            "Pega la descripción del puesto o requisitos clave:",
            height=200,
            placeholder="Ejemplo: Se busca Ingeniero de Software con conocimientos de Python, APIs de IA y automatización. Orientación a negocio..."
        )
        
    if st.button("🚀 Analizar Candidato", type="primary"):
        if not cv_text:
            st.error("Por favor, sube un CV válido antes de continuar.")
        elif not job_description:
            st.error("Por favor, introduce la descripción de la oferta.")
        else:
            with st.spinner("Analizando currículum y comparándolo con los requisitos..."):
                # Configurar parser estructurado
                parser = JsonOutputParser(pydantic_object=CandidateEvaluation)
                
                # Definir Prompt Template
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "Eres un consultor experto en selección técnica en Tessera. Tu tarea es analizar objetivamente el currículum del candidato y evaluar su encaje con los requisitos del puesto.\n\nFormato de salida requerido:\n{format_instructions}"),
                    ("human", "CURRÍCULUM DEL CANDIDATO:\n{cv_text}\n\nREQUISITOS DEL PUESTO:\n{job_description}")
                ])
                
                # Construir la cadena
                chain = prompt | llm | parser
                
                try:
                    evaluation = chain.invoke({
                        "cv_text": cv_text,
                        "job_description": job_description,
                        "format_instructions": parser.get_format_instructions()
                    })
                    
                    # --- MOSTRAR RESULTADOS ---
                    st.success("🎉 ¡Análisis Completado!")
                    
                    # Fila superior: Score y Resumen Ejecutivo
                    res_col1, res_col2 = st.columns([1, 2])
                    
                    with res_col1:
                        # Tarjeta visual de match score
                        score = evaluation.get("match_score", 0)
                        st.markdown(f"""
                        <div class="metric-card">
                            <h4>Porcentaje de Encaje</h4>
                            <div class="metric-value">{score}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with res_col2:
                        st.subheader("Resumen Ejecutivo de la Recomendación")
                        st.write(evaluation.get("summary", "No se pudo generar el resumen."))
                    
                    st.markdown("---")
                    
                    # Fila media: Puntos Fuertes y Gaps
                    col_det1, col_det2 = st.columns(2)
                    with col_det1:
                        st.subheader("💪 Puntos Fuertes")
                        for strength in evaluation.get("strengths", []):
                            st.markdown(f"- ✅ {strength}")
                            
                    with col_det2:
                        st.subheader("⚠️ Áreas de Mejora o Gaps")
                        for gap in evaluation.get("gaps", []):
                            st.markdown(f"- 🔍 {gap}")
                    
                    st.markdown("---")
                    
                    # Fila inferior: Guion de entrevista
                    st.subheader("📋 Preguntas de Entrevista Sugeridas")
                    st.write("Diseñadas especialmente para este candidato en función de los puntos débiles de su CV:")
                    for idx, question in enumerate(evaluation.get("interview_questions", []), 1):
                        st.info(f"**Pregunta {idx}:** {question}")
                        
                except Exception as e:
                    st.error(f"Ocurrió un error durante el procesamiento de IA: {e}")

# ==========================================
# TAB 2: INVESTIGADOR Y REDACTOR COMERCIAL
# ==========================================
with tab2:
    st.header("🔍 Investigador de Empresas & Redactor Comercial")
    st.write("Optimiza tu prospección. Introduce los datos de una empresa a la que Tessera quiera ofrecer servicios; la IA investigará sus novedades en la web y redactará una propuesta comercial personalizada por email.")
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        company_name = st.text_input("Nombre de la Empresa", placeholder="Ejemplo: Cabify, Glovo, Inditex...")
        company_website = st.text_input("Sitio Web (Opcional)", placeholder="Ejemplo: cabify.com")
        
    with col_input2:
        pitch_focus = st.text_area(
            "Foco de la propuesta (Pitch)",
            height=100,
            placeholder="Ejemplo: Ofrecerles automatizar su cribado de selección con IA o modernizar sus pipelines de datos...",
            value="Ayudarles a optimizar su departamento de selección y operaciones internas mediante el uso de agentes de IA y automatizaciones a medida."
        )
        
    if st.button("🔍 Investigar y Generar Email", type="primary"):
        if not company_name:
            st.error("Por favor, introduce el nombre de la empresa a investigar.")
        else:
            with st.spinner(f"Investigando a '{company_name}' en internet..."):
                # Ejecutar la búsqueda
                search_results, engine_used = search_company_info(company_name, company_website, tavily_key)
                
                st.info(f"📍 Motor de búsqueda utilizado: **{engine_used}**")
                with st.expander("Ver fragmentos web recopilados"):
                    st.text(search_results)
                
            with st.spinner("Redactando email comercial personalizado..."):
                # Diseñar prompt para la redacción
                outreach_prompt = ChatPromptTemplate.from_messages([
                    ("system", """Eres Sergio Bardavio, especialista en tecnología y automatización en Tessera. Tu objetivo es redactar un email frío altamente personalizado a un directivo de la empresa objetivo.
                    Debes utilizar la información recopilada en la búsqueda web sobre la empresa para hacer una referencia real, demostrando que les has investigado (proyectos recientes, cultura, etc.).
                    Propón el servicio indicado por el usuario (foco del pitch). El tono debe ser profesional, cercano, dinámico y muy orientado a resultados de negocio (enfoque Informática + ADE).
                    Escribe el correo en español. Incluye un asunto (Subject) muy llamativo e irresistible al principio del mensaje."""),
                    ("human", "EMPRESA A CONTACTAR:\nNombre: {company_name}\nWeb: {company_website}\n\nINFORMACIÓN ENCONTRADA EN LA WEB:\n{search_results}\n\nFOCO DE LA PROPUESTA:\n{pitch_focus}")
                ])
                
                chain = outreach_prompt | llm
                
                try:
                    email_draft = chain.invoke({
                        "company_name": company_name,
                        "company_website": company_website,
                        "search_results": search_results,
                        "pitch_focus": pitch_focus
                    })
                    
                    st.success("✉️ ¡Borrador del Email Generado con éxito!")
                    st.subheader("Borrador de Email Comercial")
                    st.text_area("Copia el texto del email aquí:", value=email_draft.content, height=400)
                    
                    st.caption("💡 **Tip de Ventas:** Este email está personalizado con la información web recopilada arriba, lo que incrementa la tasa de respuesta en frío frente a plantillas genéricas.")
                except Exception as e:
                    st.error(f"Error al redactar el correo: {e}")
