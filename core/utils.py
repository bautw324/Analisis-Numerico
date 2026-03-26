import numpy as np
import re, io
from fpdf import FPDF
import streamlit as st
from core import grafico

def evaluar_f(formula, x=0):
    formula_python = formula.replace('^', '**').replace(',', '.')
    formula_python = re.sub(r'(\d)x', r'\1*x', formula_python)

    # Definimos el diccionario de variables y funciones permitidas
    entorno_seguro = {
        'x': x,
        'np': np,
        'sin': np.sin,
        'sen': np.sin,
        'cos': np.cos,
        'exp': np.exp,
        'log': np.log,
        'e': np.e,
        'pi': np.pi
    }

    # Intentamos evaluar la fórmula
    try:
        return eval(formula_python, entorno_seguro)
        
    except SyntaxError:
        raise ValueError("Error de sintaxis. Verifica que la fórmula esté completa y bien escrita (ej: te falta un número o cerraste mal un paréntesis).")
        
    except NameError as e:
        variable_falsa = str(e).split("'")[1] if "'" in str(e) else str(e)
        raise ValueError(f"No reconozco el término '{variable_falsa}'. Asegurate de usar solo la variable 'x' y funciones válidas (sin, cos, exp, etc.).")
        
    except ZeroDivisionError:
        raise ValueError("División por cero detectada en este punto. La función diverge o no está definida aquí.")
        
    except Exception as e:
        raise ValueError(f"Error matemático al calcular: {e}")

def mostrar_formula(formula):
    f = formula.replace('**','^').replace('sen','sin').replace('.', ',')

    f = re.sub(r'\((.*?)\)/\(?([a-zA-Z0-9.x\s\+\-\*]+)\)?', r'\\frac{\1}{\2}', f)

    f = re.sub(r'\^\((.*?)\)', r'^{\1}', f)
    
    f = re.sub(r'(\d)x',r'\1*x',f)

    funciones = r'(sin|cos|exp|log|pi)'
    
    f = re.sub(funciones, r'\\\1', f)

    f = f.replace('*', r' \cdot ')

    return f'f(x) = {f}'

@st.cache_data(show_spinner=False)
def generar_pdf_reporte(metodo, formula, parametros, raiz, historial_dict, fig):
    pdf = FPDF()
    pdf.add_page()
    
    # --- 1. TÍTULO Y FUENTE ESTÉTICA ---
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(30, 136, 229) # Azul Rooty
    pdf.cell(0, 10, "Reporte de Análisis Numérico - Rooty", new_x="LMARGIN", new_y="NEXT", align="C")
    
    # Línea separadora
    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(8)

    # --- 2. DATOS DEL PROBLEMA ---
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(60, 60, 60) 
    pdf.cell(0, 8, f"Método de {metodo}: f(x) = {formula}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Parámetros: {parametros}", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(39, 174, 96) # Verde éxito
    pdf.cell(0, 10, f"Raíz encontrada: x = {raiz:.6f}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # --- 3. EL GRÁFICO ---
    if fig is not None:
        img_bytes = fig.to_image(format="png", width=800, height=400, scale=2)
        imagen_virtual = io.BytesIO(img_bytes)
        pdf.image(imagen_virtual, w=190)
        pdf.ln(8) 

    # --- 4. LA TABLA PREMIUM (CON ÍNDICES) ---
    if historial_dict:
        # Extraemos las columnas originales (ej: 'x[i]')
        columnas_orig = list(historial_dict.keys())
        
        # Limpiamos los nombres para el PDF (Cambia 'x[i]' por 'x_i')
        columnas_limpias = [col.replace("[i]", "_i") for col in columnas_orig]
        
        # Sumamos 1 al número de columnas para hacerle lugar al índice "Iter"
        num_cols = len(columnas_orig) + 1 
        ancho_col = 190 / num_cols 
        
        # Diseño del Encabezado
        pdf.set_fill_color(30, 136, 229)
        pdf.set_text_color(255, 255, 255)
        pdf.set_draw_color(30, 136, 229) 
        pdf.set_font("helvetica", "B", 11)
        
        # Agregamos la primera columna a mano: "Iter"
        pdf.cell(ancho_col, 8, "Iter", border=1, align="C", fill=True)
        # Agregamos el resto de las columnas limpias
        for col_nombre in columnas_limpias:
            pdf.cell(ancho_col, 8, col_nombre, border=1, align="C", fill=True)
        pdf.ln()

        # Diseño de las Filas
        pdf.set_text_color(40, 40, 40) 
        pdf.set_draw_color(220, 220, 220) 
        pdf.set_font("helvetica", "", 10)
        
        num_filas = len(historial_dict[columnas_orig[0]])
        for i in range(num_filas):
            
            # Protección de Salto de Página
            if pdf.get_y() > 270:
                pdf.add_page()
                pdf.set_fill_color(30, 136, 229)
                pdf.set_text_color(255, 255, 255)
                pdf.set_font("helvetica", "B", 11)
                pdf.cell(ancho_col, 8, "Iter", border=1, align="C", fill=True)
                for col_nombre in columnas_limpias:
                    pdf.cell(ancho_col, 8, col_nombre, border=1, align="C", fill=True)
                pdf.ln()
                pdf.set_text_color(40, 40, 40)
                pdf.set_font("helvetica", "", 10)

            # Efecto Cebra
            if i % 2 == 0:
                pdf.set_fill_color(248, 248, 248) 
            else:
                pdf.set_fill_color(255, 255, 255) 
                
            # 1. Imprimimos el número de iteración (0, 1, 2...)
            pdf.cell(ancho_col, 8, str(i), border="LR", align="C", fill=True)
            
            # 2. Imprimimos los datos de la fila
            for col_orig in columnas_orig:
                valor = historial_dict[col_orig][i]
                texto = f"{valor:.6f}" if isinstance(valor, float) else str(valor)
                pdf.cell(ancho_col, 8, texto, border="LR", align="C", fill=True)
            pdf.ln()
            
        # Línea final de la tabla
        pdf.cell(ancho_col * num_cols, 0, "", border="T")

    return bytes(pdf.output())

def boton_descarga(metodo, formula, parametros, raiz, datos, fig):
    if st.button('Generar reporte en PDF',key='generar_repo',type='secondary', icon='📝'):
        # Generamos el PDF en crudo (los bytes)
        with st.spinner('Generando reporte PDF...',show_time=True):
            pdf_bytes = generar_pdf_reporte(
                metodo=metodo,
                formula=formula,
                parametros=parametros,
                raiz=raiz,
                historial_dict=datos,
                fig=fig
            )
        st.download_button(
            label="Descargar Reporte en PDF",
            data=pdf_bytes,
            file_name=f"Reporte_{metodo}_{raiz:.4f}.pdf",
            mime="application/pdf",
            type="primary", # Lo pinta del color principal de tu app
            icon="📄"
        )

def mostrar_panel_resultados(raiz, datos, grafico_f, converge=True):       
    st.space('small')
    if converge:
        st.success(f'Raíz encontrada en: $x \\approx {raiz:.6f}$')
        # Gráfico
        with st.spinner(text='Generando grafica...'):
            grafico.dibujar(grafico_f)
        
        # Expander para la tabla
        with st.expander("Ver tabla de iteraciones"):
            st.dataframe(datos,width='stretch',hide_index=False)
    else:
        st.error('El método DIVERGIÓ o no alcanzó la tolerancia requerida.')
        st.info('💡 Intentá cambiar el punto inicial o los parámetros.')
        st.warning(f'Último valor calculado: $x \\approx {raiz:.6f}$')
