import numpy as np
import utils as ec
import plotly.graph_objects as go

def dibujar(f,raiz,inf,sup):
    x = np.linspace(inf, sup, 300)
    y = ec.evaluar_f(f,x)
    fig = go.Figure()
    ymin, ymax = float(np.min(y)), float(np.max(y))
    x_grids = np.linspace(inf, sup, 11)
    y_grids = np.linspace(ymin, ymax, 11)
    
    fig.update_layout(
        dragmode=False,
        xaxis=dict(
            title='Eje X',
            showgrid=False,
            zeroline=False,
            layer='below traces',
        ),
        yaxis=dict(
            title='Eje Y',
            showgrid=False,
            zeroline=False,
            layer='below traces'
        )
    )
    # líneas de cuadrícula como shapes en el nivel más bajo
    for xi in x_grids:
        fig.add_shape(dict(
            type='line', x0=xi, x1=xi, y0=ymin, y1=ymax,
            line=dict(color='lightgray', width=1, dash='dot'),
            layer='below'
        ))
    for yi in y_grids:
        fig.add_shape(dict(
            type='line', x0=inf, x1=sup, y0=yi, y1=yi,
            line=dict(color='lightgray', width=1, dash='dot'),
            layer='below'
        ))
    
    # La función se dibuja encima de ejes y cuadrícula
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x)', line=dict(color='blue', width=2)))
    
    fig.add_vline(x=0, line_color="red", line_width=1, line_dash="solid", opacity=1, layer='below')
    
    fig.add_hline(y=0, line_color="red", line_width=1, line_dash="solid", opacity=1, layer='below')
    
    fig.add_trace(go.Scatter(
        x=[raiz], 
        y=[0],
        mode='markers',
        name='Raíz',
        marker=dict(
            size=10,
            color='green',
            symbol='circle',
            line=dict(color='black', width=1)
        )
    ))
    return fig