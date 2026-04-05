import streamlit as st
import inicio
from core import utils as ut

# Importamos las CLASES, no los módulos
from metodos.biseccion import Biseccion
from metodos.regula_falsi import Regula_Falsi
from metodos.newton import Newton
from metodos.punto_fijo import PuntoFijo
from metodos.secante import Secante
from metodos.regresion import Regresion
from metodos.comparacion import Comparacion

st.set_page_config(
    page_title='Roooty',
    page_icon='📊',
    layout='wide'
)

# Instanciamos cada método una sola vez
# Para agregar uno nuevo: solo agregarlo acá
METODOS = [
    Biseccion(),
    Regula_Falsi(),
    Newton(),
    PuntoFijo(),
    Secante(),
    Regresion(),
    Comparacion()
]
import streamlit as st 
# Construimos el diccionario dinámicamente desde las propiedades de cada clase
# La key es "Bisección", "Newton", etc.
METODOS_DICT = {f"{m.nombre}": m for m in METODOS}

# --- CSS ---

import streamlit as st
# (Mantené tus imports originales acá arriba: import inicio, from core import utils, etc.)

def cargar_css(ruta_archivo):
    with open(ruta_archivo, encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

cargar_css("estilos.css")

def main():
    # --- MENÚ LATERAL SEGURO Y LIMPIO ---
    with st.sidebar:
        # Logo Corporativo
        st.markdown("""
            <div style="display: flex; align-items: center; margin-bottom: 2rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 1rem;">
                <h1 style="margin: 0; font-weight: 800; color: #1a2b4c; font-size: 1.8rem; letter-spacing: -1px;">Σ ROOOTY LAB</h1>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='color: #64748b; font-weight: bold; font-size: 0.8rem; margin-bottom: 0.5rem;'>NAVEGACIÓN</p>", unsafe_allow_html=True)
        
        # Armamos las opciones de forma segura usando emojis en vez de HTML
        opciones_seguras = ["🏠 Inicio"]
        for metodo in METODOS_DICT.keys():
            opciones_seguras.append(f"⚙️ {metodo}")
            
        # El radio clásico que NUNCA falla
        eleccion_cruda = st.radio(
            "Menú", 
            options=opciones_seguras,
            label_visibility="collapsed"
        )
        
        st.markdown("<hr style='border: 1px solid #f1f5f9; margin: 2rem 0;'>", unsafe_allow_html=True)

        st.markdown("<p style='color: #64748b; font-weight: bold; font-size: 0.8rem; margin-bottom: 0.5rem;'>UTILIDADES</p>", unsafe_allow_html=True)
        ut.mostrar_menu_ajustes() 

    # --- LÓGICA PARA LIMPIAR EL NOMBRE DEL MÉTODO ---
    if eleccion_cruda == "🏠 Inicio":
        choice = "Inicio"
    else:
        # Le sacamos el emoji y el espacio para que coincida con tu diccionario
        choice = eleccion_cruda.replace("⚙️ ", "")

    # --- PANTALLA PRINCIPAL ---
    if choice == "Inicio":
        inicio.inicio() 
    else:
        st.markdown(f"<h2 style='color: #1a2b4c; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; font-weight: 800;'>{choice}</h2>", unsafe_allow_html=True)
        
        if st.session_state.get('mostrar_pdf', False):
            st.pdf("archivos/Consigna Tp 1 inf tele.pdf")
        
        METODOS_DICT[choice].mostrar_info()

if __name__ == '__main__':
    main()