import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def evaluar_f(formula,x):
    formula_python = formula.replace('^','**')
    return eval(formula_python, {
        'x':x,
        'np':np,
        'sin':np.sin,
        'cos':np.cos,
        'exp':np.exp,
        'log':np.log
    })

def biseccion(f,a,b,err,max_i):
    # Casos base
    if evaluar_f(f,a)*evaluar_f(f,b)>0:
        return None
    x = (a+b)/2
    if abs(evaluar_f(f,x)) < err or max_i<=0: 
        return x
    # Opciones
    if evaluar_f(f,x) * evaluar_f(f,a) < 0:
        x = biseccion(f,a,x,err,max_i-1)
    else:
        x = biseccion(f,x,b,err,max_i-1)
    return x

def mostrar_info():
    st.header('Metodo Bisección')
    
    formula = st.text_input('Escribe tu función $f(x)$:', value='x**2 + 11*x - 6')
    st.caption("Usa `**` para potencias (ej: `x**2`) y `*` para productos. También puedes usar `sin(x)`, `exp(x)`, etc.")
    
    formula_muestra = 'f(x)=' + formula.replace('**','^').replace('*','')
    st.latex(formula_muestra)
    
    col1, col2 = st.columns(2)
    with col1:
        inf = st.number_input('Ingresar intervalo inferior',value=-10.0,step=0.5)
        err = st.number_input('Ingresar tolerancia de error',value=0.01,min_value=0.01)
    with col2:
        sup = st.number_input('Ingresar intervalo superior',value=10.0,step=0.5)
        max_i = st.number_input('Ingresar cantidad de iteraciones',min_value=1,max_value=30,value=5)
    try:
        x = np.linspace(inf, sup, 100)
        y = evaluar_f(formula,x)
        
        fig, ax = plt.subplots()
        p_x = biseccion(formula,inf,sup,err,max_i)
        
        if p_x is not None:
            ax.scatter(p_x,0.0,color='green', s=30, zorder=5, label="Punto")
            st.success(f'Raíz encontrada en: $$x ≈ {p_x}$$')
            # st.balloons()
        else:
            st.error('No se ha encontrado la raíz.')

        ax.plot(x, y, label='$f (x)$', color='skyblue', linewidth=2)
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()
        ax.grid(True)
        
        # Mostrar la figura en Streamlit
        st.pyplot(fig)
    except Exception as e:
        st.error(f'Error en la fórmula: {e}')
        st.info('Escribe la fórmula correctamente. Ejemplo: `x**2 + 11*x - 6`')
    
    st.subheader('Código hecho en Python')
    st.code('''
def biseccion(a,b,err,max_i):
# Casos base
if f(a)*f(b)>0:
    return None
x = (a+b)/2
if abs(f(x)) < err or max_i<=0: 
    return x
# Opciones
if f(x) * f(a) < 0:
    x = biseccion(a,x,err,max_i-1)
else:
    x = biseccion(x,b,err,max_i-1)
return x''',
            "python")