from abc import ABC, abstractmethod
import streamlit as st
from core import grafico, utils as ut

class MetodoNumerico(ABC):
    
    @property
    @abstractmethod
    def nombre(self):
        """Nombre del método. Ej: 'Bisección'"""
        pass
    
    # En la clase base - por defecto el toggle de las iteraciones existe
    @property
    def tiene_toggle(self):
        return True
    
    @abstractmethod
    def ejecutar(self, f, err, **params):
        """
        Corre el algoritmo y devuelve (raiz, datos).
        El parematro **params es como una mochila.
        Los ** le dicen a Python "todo lo que me manden de más, metelo en un diccionario llamado params"
        """
        pass
    
    @abstractmethod
    def render_teoria(self):
        """Muestra un fragmento en donde se explica detalladamente en que consiste el código."""
        pass
    
    @abstractmethod
    def render_inputs(self, key=None):
        """Dibuja los inputs de Streamlit y devuelve los parámetros."""
        pass
                    
    @abstractmethod
    def mostrar_codigo(self):
        """Muestra un extracto del código en Python."""
        pass
    
    @abstractmethod
    def get_rango_grafico(self, raiz, **params):
        """Devuelve (inf, sup) para el gráfico según el método."""
        pass

    def get_formula_grafico(self, f):
        """Por defecto, f ya es un string. Regresión lo pisa."""
        return f

    def render_formula(self, valor_default = 'x**2 + 11*x - 6'):
        f = st.text_input('Función $f(x)$:', value=valor_default)
        st.caption("Usa `( )` para agrupar elementos. Por ejemplo `e^(1-x)` para $$ e^{1-x}$$.")
        
        st.latex(ut.mostrar_formula(self.get_formula_grafico(f)))
        
        exponente_err = st.select_slider(
            "Presición",
            options=[1,2,3,4,5,6,7,8,9,10],
            value=2,
            format_func=lambda x: f"$10^{{{-int(x)}}}$"
            )
        # Por ejemplo: 10^(-2)
        err = 10**(-exponente_err)
        return f, err, exponente_err
    
    def mostrar_resultados(self, raiz, datos, grafico_f):
        st.success(f'Raíz encontrada en: $x \\approx {raiz:.6f}$')
        # Gráfico
        with st.spinner(text='Generando grafica...'):
            grafico.dibujar(grafico_f)
        
        # Expander para la tabla
        with st.expander("Ver tabla de iteraciones"):
            st.dataframe(datos.obtener_dataframe(),width='stretch',hide_index=False)

    def mostrar_info(self):
        """
        Muestra la página completa del método:
            1. Título
            2. Expander de teoría
            3. Contenedor con dos columnas:
                - Entradas: formula + inputs únicos + botón PDF
                - Resultados: gráfico + tabla
            4. Sección de código Python
        """
        
        # --- 1. ZONA DEL TÍTULO ---
        st.markdown(f"<h1 style='text-align: center;'>Método {self.nombre}</h1>", unsafe_allow_html=True)
        
        # --- 2. ZONA DE TEORÍA ---
        self.render_teoria()
        
        
        with st.container(border=True):
            # Dividimos la pantalla: 1 parte para inputs, 2 partes para gráficos
            col_input, col_result = st.columns([1, 2], gap="large")

            # --- 3. ZONA ENTRADA DE DATOS ---
            with col_input:
                st.subheader("📥 Ingreso de datos")
                f, err, exponente_err = self.render_formula()
                 
                params = self.render_inputs(key=self.nombre)
                
                try:
                    st.divider()
                    
                    raiz, datos = self.ejecutar(f,err,**params)
                    if raiz is not None:
                        # Usamos un Toggle (interruptor) para prender/apagar los puntos
                        mostrar_datos = st.toggle("Mostrar iteraciones en el gráfico") if self.tiene_toggle else True
                        
                        inf, sup = self.get_rango_grafico(raiz=raiz,**params)
                        
                        # Esto es por si alguna formula no está en este formato
                        formula_str = self.get_formula_grafico(f)
                        
                        grafico_f = grafico.obtener_grafico(formula_str, raiz, inf, sup, key=f'graf_{self.nombre.lower()}', iteraciones=datos.obtener_datos() if mostrar_datos else None)
                        
                        ut.boton_descarga(
                            metodo=self.nombre,
                            formula=f,
                            params=params,
                            # parametros=f"Intervalo del grafico [{inf}; {sup}], Tolerancia: 10^-{exponente_err}",
                            raiz=raiz,
                            datos=datos.obtener_datos(),
                            fig=grafico_f
                            )
                    
                except Exception as e:
                    raiz = None
                    st.error(f'Error en la fórmula: {e}')
                    st.info('Escribe la fórmula correctamente. Ejemplo: `x**2 + 11*x - 6`')
                    
            # --- 3. ZONA DE GRÁFICOS Y RESULTADOS ---
            with col_result:
                # Verifica si existe la raíz antes de mostrar opciones adicionales
                if 'raiz' in locals() and raiz is not None:
                    self.mostrar_resultados(raiz=raiz,datos=datos,grafico_f=grafico_f)
                        
                else:
                    if 'raiz' in locals():
                        st.error('No se ha encontrado la raíz.')    
        st.divider()
        
        # --- 4. ZONA DEL CÓDIGO EN PYTHON ---
        st.header('Código en Python')
        self.mostrar_codigo()
