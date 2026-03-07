import streamlit as st
import pandas as pd
import biseccion

st.set_page_config(page_title='App Análisis Numerico',page_icon='📊',initial_sidebar_state='collapsed')

def main():

    st.title('App Análisis Numérico 📊')
    
    menu = ['Bisección','Inicio']
    
    choice = st.sidebar.selectbox('Menú',menu)
    
    if choice == 'Inicio':
        st.subheader('Inicio')
    elif choice == 'Bisección':
        biseccion.mostrar_info()

if __name__ == '__main__':
    main()
