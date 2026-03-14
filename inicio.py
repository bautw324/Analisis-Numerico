import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import json
def cargar_lottie_local(ruta_archivo: str):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return json.load(f)
def inicio():
    lottie_welcome = cargar_lottie_local("animaciones/Welcome.json")
    st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
    if lottie_welcome:
        
        st_lottie(
            lottie_welcome,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=200, 
            width=None, 
            key="large_welcome_animation",
        )
    st.markdown('</div>', unsafe_allow_html=True)
    
    #st.header('Introducción')
    st.write("""
    - **Materia:** Análisis Numérico
    - **Docente:** Mauricio Orellana
    - **Objetivo general:** Desarrollar, implementar y analizar métodos numéricos aplicados a problemas reales.
    """)
    
    st.divider()

    st.header("👥 Integrantes del Equipo")

    data = {
        "Integrante": ["Bauti", "Mica", "Juan", "Net", "Trini", "Brisa", "Manu"],
        "Rol": ["Desarrollo", "Coordinación", "Documentación", "Testing", "Diseño", "Revisión", "Comunicación"],
    }

    df_integrantes = pd.DataFrame(data)
    st.dataframe(df_integrantes,hide_index=True)

    st.divider()

    st.header("🎯 Objetivos del Grupo")

    st.write("""
    - Comprender y aplicar métodos numéricos fundamentales.  
    - Desarrollar implementaciones en Python/Streamlit.  
    - Documentar resultados y análisis.  
    - Fomentar el trabajo colaborativo y la revisión cruzada.
    """)

    st.divider()

    st.header("🛠️ Herramientas Utilizadas")

    st.write("""
    - **Lenguajes:** Python  
    - **Librerías:** NumPy, SciPy, Matplotlib, Pandas  
    - **Plataformas:** GitHub, Streamlit  
    - **Metodologías:** Control de versiones, issues, branches
    """)

    st.divider()

    st.header("📚 Contenidos Abordados")

    st.write("""
    - Error numérico y estabilidad  
    - Métodos para ecuaciones no lineales  
    - Interpolación y aproximación
    """)

    st.divider()

    st.header("🧪 Actividades y Proyectos Realizados")

    st.write("""
    - Implementación de métodos numéricos en Python  
    - Desarrollo de una app interactiva en Streamlit  
    - Análisis de resultados y comparación de métodos  
    - Documentación en GitHub
    """)

    st.divider()

    st.header("📈 Resultados y Conclusiones")

    st.write("""
    - Se lograron implementar correctamente los métodos estudiados.  
    - Se identificaron desafíos en estabilidad y convergencia.  
    - El trabajo colaborativo permitió mejorar la calidad del código.  
    - Se proponen mejoras para futuras versiones de la app.
    """)
