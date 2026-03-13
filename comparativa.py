import streamlit as st
import grafico
import pandas as pd
import biseccion, secante

def comparar_sec_bis(formula, inf, sup, err, mostrar_datos=False):
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        raiz_bis, datos_bis = biseccion.biseccion(formula,inf,sup,err)
        st.subheader('Biseccion')
        st.success(f'Raíz en: $$x ≈ {round(raiz_bis,6)}$$')     
        grafico.dibujar(formula, raiz_bis, inf, sup, key="grafico_biseccion", iteraciones=datos_bis if mostrar_datos else None)
        if mostrar_datos:
            st.dataframe(pd.DataFrame(datos_bis)) 
        
    with col2:
        raiz_sec, datos_sec = secante.secante(formula,inf,sup,err)
        st.subheader('Secante')
        st.success(f'Raíz en: $$x ≈ {round(raiz_sec,6)}$$')  
        grafico.dibujar(formula, raiz_sec, inf, sup, key="grafico_secante", iteraciones=datos_sec if mostrar_datos else None)
        if mostrar_datos:
            st.dataframe(pd.DataFrame(datos_sec))