import plotly.graph_objects as go
import streamlit as st
import numpy as np
import utils as ec

def dibujar(f, raiz, inf, sup, key=None, iteraciones=None):
    # Calculamos la distancia más larga desde la raíz a los extremos
    # para que al usarla en ambos lados, la raíz quede en el centro exacto.
    distancia_a_inf = abs(raiz - inf)
    distancia_a_sup = abs(raiz - sup)
    radio_vista = max(distancia_a_inf, distancia_a_sup)
    
    # Le sumamos un pequeño margen (10%) para que no toque los bordes
    radio_con_margen = radio_vista * 1.1

    # Generamos los puntos basados en ese radio para que la curva no se corte
    x = np.linspace(raiz - radio_con_margen, raiz + radio_con_margen, 1000)
    y = ec.evaluar_f(f, x)
    
    fig = go.Figure()

    # Función f(x)
    fig.add_trace(go.Scatter(
        x=x, y=y, 
        mode='lines', 
        name='f(x)', 
        line=dict(color='#1E88E5', width=3)
    ))

    if iteraciones is not None and 'x[i]' in iteraciones:
        x_puntos = iteraciones['x[i]'][:-1]  # Excluimos el último punto que es la raíz aproximada
        # Creamos los índices dinámicos: x_0, x_1, x_2...
        etiquetas = [f"x_{i}" for i in range(len(x_puntos))]
        
        fig.add_trace(go.Scatter(
            x=x_puntos,
            y=[0] * len(x_puntos), # <--- ESTO las mantiene sobre el eje X
            mode='markers',
            text=etiquetas,
            textposition="top center", # Las etiquetas quedan arriba de la 'x'
            name='Rastro x_i',
            marker=dict(
                symbol='x', 
                size=10, 
                color='#EF4444', # Rojo vibrante para resaltar
                line=dict(color='white', width=1)
            ),
            textfont=dict(
                family="Inter, sans-serif",
                size=9,
                color="#EF4444"
            ),
            # Evita que el cartelito de hover sea molesto
            hovertemplate="Iteración %{text}: %{x:.6f}<extra></extra>"
        ))

    # Raíz (El centro del mundo)
    fig.add_trace(go.Scatter(
        x=[raiz], y=[0],
        mode='markers',
        name='Raíz Aproximada',
        marker=dict(size=12, color='#00E676', line=dict(color='white', width=2))
    ))
    
    # Línea punteada para el límite inferior 'a'
    fig.add_vline(
        x=inf, 
        line_width=2, 
        line_dash="dash",
        line_color="rgba(30, 136, 229, 0.5)"
    )

    # Línea punteada para el límite superior 'b'
    fig.add_vline(
        x=sup, 
        line_width=2, 
        line_dash="dash", 
        line_color="rgba(30, 136, 229, 0.5)"
    )

    fig.update_layout(
        template='plotly_white',
        dragmode=False, 
        hovermode='x unified',
        margin=dict(l=40, r=40, t=100, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5),
        
        xaxis=dict(
            # Aplicamos el rango simétrico respecto a la raíz
            range=[raiz - radio_con_margen, raiz + radio_con_margen],
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.2)',
            zeroline=True,
            zerolinecolor='rgba(176, 196, 222, 0.8)', 
            zerolinewidth=2.5
        ),
        yaxis=dict(
            range = [-max(abs(y))*1.2, max(abs(y))*1.2],
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.2)',
            zeroline=True,
            zerolinecolor='rgba(176, 196, 222, 0.8)',
            zerolinewidth=2.5
        )
    )
    st.plotly_chart(
                fig, 
                use_container_width=True,
                key=key,
                config={
                    'scrollZoom': False,
                    'displayModeBar': True,
                    'displaylogo': False,
                    'showTips': False,
                    'modeBarButtons': [[
                        'zoomIn2d', 
                        'zoomOut2d', 
                        'resetViews'
                    ]]
                }
            )