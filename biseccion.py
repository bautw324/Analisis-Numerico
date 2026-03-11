import streamlit as st
import numpy as np
import utils as ec
import pandas as pd
import plotly.graph_objects as go
import grafico

def biseccion(f,a,b,err):
    cuadro = {
    'a[i]':[],
    'b[i]':[],
    'x[i]':[],
    'f(x[i])':[],
    'Dx[i]':[]
    }
    fa = ec.evaluar_f(f,a)
    fb = ec.evaluar_f(f,b)

    # Casos base
    if fa * fb > 0:
        return None, []
    if a  > b:
        a, b = b, a
        fa, fb = fb, fa
    
    # Calculo de la raíz
    x_anteior = a
    while True:
        x = (a+b)/2
        fx = ec.evaluar_f(f,x)

        cuadro['a[i]'].append(a)
        cuadro['b[i]'].append(b)
        cuadro['x[i]'].append(x)
        cuadro['f(x[i])'].append(fx)
        cuadro['Dx[i]'].append(x-a)

        if abs(fx) < err: 
            return x, cuadro
        if round(x,6) == round(x_anteior,6):
            break
        
        x_anteior = x
        
        # Opciones
        if fx * fa < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    return x, cuadro

def mostrar_info():
    st.header('Metodo Bisección')
    
    formula = st.text_input('Escribe tu función $f(x)$:', value='x**2 + 11*x - 6')
    
    st.latex(ec.mostrar_formula(formula))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        inf = st.number_input('Ingresar intervalo inferior',value=-5.0,step=2.0)
    with col2:
        sup = st.number_input('Ingresar intervalo superior',value=5.0,step=2.0)
    with col3:
        err = st.number_input('Tolerancia de error $E = 10^{-n}$',value=2,min_value=1, max_value=10)
        err = 10**(-err)
    try:
        raiz, datos = biseccion(formula,inf,sup,err)
        
        if raiz is not None:
            st.success(f'Raíz encontrada en: $$x ≈ {round(raiz,6)}$$')

            st.plotly_chart(
                grafico.dibujar(formula,raiz,inf,sup),
                config={
                'scrollZoom': False,
                'staticPlot': False
            })
                
            mostrar_datos = st.checkbox("Mostrar datos de iteraciones")
            
            if mostrar_datos:
                st.dataframe(pd.DataFrame(datos))
        else:
            st.error('No se ha encontrado la raíz.')

    except Exception as e:
        st.error(f'Error en la fórmula: {e}')
        st.info('Escribe la fórmula correctamente. Ejemplo: `x**2 + 11*x - 6`')

    st.divider()
    st.header('Código hecho en Python')
    st.code('''
def biseccion(f,a,b,err,max_i):
    fa = f(a)
    fb = f(b)
    # Casos base
    if f(a) * f(b) > 0:
        return None
    if a  > b:
        a, b = b, a
    # Calculo de la raíz
    for i in range(1, max_i+1):
        x = (a+b)/2
        fx = f(x)
        if abs(fx) < err or max_i<=0: 
            return x
        # Opciones
        if fx * fa < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    return x''',
            "python")