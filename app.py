import streamlit as st
import inicio
from core import utils as ut
from metodos import biseccion, secante, newton, punto_fijo, regresion, comparacion, tangente

st.set_page_config(
    page_title='Roooty',
    page_icon='📊',
    layout='wide'
)

METODOS = {
    "Bisección":biseccion,
    "Secante":secante, 
    "Newton":newton, 
    "Tangente":tangente, 
    "Punto Fijo":punto_fijo, 
    "Regresión":regresion, 
    "Comparación":comparacion
}

# --- CSS ---
estilo = """
    <style>
    /* Ocultar barra superior por defecto */
    
    body {
        padding: 0 100px !important;
    }
    
    header {visibility: hidden !important;}
    
    /* Espaciado del contenido */
    .block-container {
        max-width: 1400px;
        padding-top: 2rem !important; 
        padding-bottom: 6rem !important; 
    }
    
    /* FOOTER CON EFECTO CRISTAL */
    .mi-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(30, 30, 30, 0.4); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px); 
        color: #888888;
        text-align: center;
        padding: 12px 0;
        font-size: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        z-index: 999; 
    }
    .mi-footer a { color: #1E88E5; text-decoration: none; font-weight: bold; }
    .mi-footer a:hover { text-decoration: underline; }
    </style>

    <div class="mi-footer">
        Desarrollado con ❤️ por el Grupo de Análisis Numérico | 
        <a href="https://github.com/BautistaGenovese/Analisis-Numerico" target="_blank">Ver código en GitHub</a>
    </div>
"""
st.markdown(estilo, unsafe_allow_html=True)
# -----------------------------------------

def main():
    with st.container(border=True):
        
        col_logo, col_nav, col_ajustes = st.columns([1.2, 3, 0.3], vertical_alignment="center") 
        
        with col_logo:
            st.markdown("""
                <div style="display: flex; margin-top:-10px;align-items: center; height: 100%; min-height: 45px; padding-left: 10px;">
                    <h3 style="margin: 0; padding: 0; line-height: 1;">📊 Roooty</h3>
                </div>
            """, unsafe_allow_html=True)
            
        with col_nav:
            choice = st.pills(
                "Navegación",
                options=list(METODOS.keys()),
                default=None,
                selection_mode='single',
                label_visibility="collapsed"
            )
            
        with col_ajustes:
            ut.mostrar_menu_ajustes()           

    st.write("") # Espacio separador
    
    # CONTENIDO DE LA APP
    if choice is None:
        inicio.inicio()
    else:
        
        if st.session_state.get('mostrar_pdf', False):
            st.pdf("archivos/Consigna Tp 1 inf tele.pdf")
        
        METODOS[choice].mostrar_info()

if __name__ == '__main__':
    main()