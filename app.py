import streamlit as st
import pandas as pd
import biseccion

st.set_page_config(page_title='App Análisis Numerico',page_icon='📊',initial_sidebar_state='collapsed')

def main():

    st.title('App Análisis Numérico 📊')

    
    choice = st.segmented_control(
        "Selecciona el módulo:",
        options=["Inicio", "Bisección"],
        default="Inicio"
    )
    
    if choice == 'Inicio':
        st.header('Introducción del Grupo')
        
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
        st.table(df_integrantes)

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
        
    elif choice == 'Bisección':
        biseccion.mostrar_info()

if __name__ == '__main__':
    main()
