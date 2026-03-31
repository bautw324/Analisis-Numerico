import streamlit as st
from core import algoritmos, grafico, utils as ut



def mostrar_info():
    st.markdown("<h1 style='text-align: center;'>Método Tangente</h1>", unsafe_allow_html=True)
    
    with st.expander("📖 ¿Cómo funciona el método de la Tangente?"):
        st.markdown("""
        **Concepto básico:** Es una alternativa al método de Newton-Raphson que aproxima la derivada. En lugar de trazar una tangente, utiliza **dos puntos iniciales** para trazar una línea **secante** a la curva. La intersección de esta línea secante con el eje X nos da la siguiente aproximación ($x_{i+1}$).
        
        **Fórmula de iteración:**
        """)
        st.latex(r"x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}")
        
        st.markdown("""
        **Intervalos permitidos y Condiciones:**
        * Requiere **dos puntos iniciales**, $x_{i-1}$ y $x_i$ (por ejemplo, $x_0$ y $x_1$).
        * A diferencia de los métodos cerrados, no es necesario que estos puntos encierren la raíz.
        * **No requiere conocer la derivada** analítica de la función $f'(x)$.
        * Al igual que Newton-Raphson, los valores iniciales deben estar relativamente cerca de la raíz para asegurar la convergencia.
        """)
        st.warning(r"⚠️ **Restricción:** La función evaluada en los dos puntos de la iteración actual no debe tener el mismo valor ($f(x_{i-1}) \neq f(x_i)$). Si son iguales, el denominador se vuelve cero, lo que significa que la línea secante es horizontal y no cruza el eje X.")
        
    with st.container(border=True):
        
        # Dividimos la pantalla: 1 parte para inputs, 2 partes para gráficos
        col_in, col_out = st.columns([1, 2], gap="large")

        with col_in:
            st.subheader("📥 Ingreso de datos")
            formula = st.text_input('Escribe tu función $f(x)$:', value='x**2 + 11*x - 6')
            st.caption("Usa `( )` para agrupar elementos. Por ejemplo `e^(1-x)` para $$ e^{1-x}$$.")
            st.latex(ut.mostrar_formula(formula))
            st.divider()

            col_1, col_2 = st.columns(2)
            with col_1:
                x_n = st.number_input('Ingresar $x_n$',value=-10.0,step=2.0)

            with col_2:    
                x_n1 = st.number_input('Ingresar $x_{n+1}$',value=-9.0,step=2.0)

            err_exp = st.select_slider(
                    "Presición",
                    options=[1,2,3,4,5,6,7,8,9,10],
                    value=2,
                    format_func=lambda x: f"$10^{{{-int(x)}}}$"
                )
            err = 10**(-err_exp)
            
            st.divider()
            try:
                raiz, datos = algoritmos.tangente(x_n1, x_n, formula, err)
                if raiz is not None:
                    
                    inf_grafico = raiz - 5
                    sup_grafico = raiz + 5
                    
                    mostrar_datos = st.toggle("Mostrar iteraciones en el gráfico")
                    
                    grafico_f = grafico.obtener_grafico(formula, raiz, inf_grafico, sup_grafico, key="graf_tangente", iteraciones=datos.obtener_datos() if mostrar_datos else None)
                    
                    ut.boton_descarga(
                        metodo='Tangente',
                        formula=formula,
                        parametros=f"Tolerancia: 10^-{err_exp}",
                        raiz=raiz,
                        datos=datos.obtener_datos(),
                        fig=grafico_f
                        )
                    
            except Exception as e:
                raiz = None
                st.error(f'Error en la fórmula: {e}')
                st.info('Escribe la fórmula correctamente. Ejemplo: `x**2 + 11*x - 6`')
        with col_out:
            # Si no eligió nada, muestra solo Newton
            if 'raiz' in locals() and raiz is not None:
                ut.mostrar_panel_resultados(raiz,datos.obtener_dataframe(),grafico_f)

            else:
                if 'raiz' in locals():
                    st.error('No se ha encontrado la raíz o no hay cambio de signo en el intervalo.')



    st.divider()
    st.header('Código hecho en Python')
    st.code('''
def tangente(x_n1, x_n, f, err):
    
    # Calculo de la raíz
    iteracion = 0
    while iteracion < 100:
        
        try:
            fx_n = ec.evaluar_f(f,x_n)
            fx_n1 = ec.evaluar_f(f,x_n1)

            x = x_n - fx_n * ((x_n - x_n1)/(fx_n - fx_n1))
            fx = ec.evaluar_f(f,x)

            if abs(fx) < err:
                return x
        
            else:
                x_n, x_n1 = x, x_n


            iteracion+=1

        except ZeroDivisionError:
            print("División por 0. Probar con otros valores.")
            return None''',
            "python")
