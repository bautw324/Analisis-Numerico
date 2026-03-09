import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import inicio, biseccion

st.set_page_config(
    page_title='App Análisis Numerico',
    page_icon='📊',
    )
mostrar_tp = False

def main():

    st.title('App Análisis Numérico 📊')

    choice = st.segmented_control(
        "Selecciona el módulo:",
        options=["Inicio", "Bisección"],
        default="Inicio"
    )

    if mostrar_tp and choice != 'Inicio':
        mostrar_tp = st.checkbox("Mostrar Consigna del TP")
        st.pdf("archivos/Consigna Tp 1 inf tele.pdf")

    if choice == 'Inicio':
        inicio.inicio()
    elif choice == 'Bisección':
        biseccion.mostrar_info()

if __name__ == '__main__':
    main()
