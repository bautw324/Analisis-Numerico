# 📊 Roooty: Software de Métodos Numéricos
Aplicación interactiva desarrollada con ❤️ en **Python + Streamlit** para la resolución de problemas de **Análisis Numérico**.
- https://roooty.streamlit.app/

## 📦 Instalación
1. Clonar el repositorio:
```bash
   git clone https://github.com/BautistaGenovese/Analisis-Numerico.git
   cd Analisis-Numerico
```
2. Crear entorno de ejecución virtual:
```bash
   python -m venv .venv
```
   Activar el entorno:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
     
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 🛫 Ejecución local
- Iniciar
   ```bash
   streamlit run app.py
   ```
- Detener
  
   Presionar `Ctrl + C`

## 📂 Estructura del Proyecto
```
Analisis-Numerico/
├── 📄 app.py                    # Punto de entrada principal
├── 📄 inicio.py                 # Pantalla de bienvenida e información del equipo
│
├── 📂 metodos/                  # Clases de los métodos numéricos (UI + lógica de vista)
│   ├── 📄 metodo_numerico.py    # Clase base abstracta (MetodoNumerico)
│   ├── 📄 biseccion.py          # Método de Bisección
│   ├── 📄 regula_falsi.py       # Método de Regula Falsi (Falsa Posición)
│   ├── 📄 newton.py             # Método de Newton-Raphson
│   ├── 📄 secante.py            # Método de la Secante
│   ├── 📄 punto_fijo.py         # Método de Punto Fijo
│   ├── 📄 regresion.py          # Regresión Lineal por Mínimos Cuadrados
│   └── 📄 comparacion.py        # Comparación cara a cara de dos métodos
│
├── 📂 core/                     # Herramientas de soporte y visualización
│   ├── 📄 algoritmos.py         # Lógica matemática pura de cada método
│   ├── 📄 grafico.py            # Trazados interactivos con Plotly
│   ├── 📄 historial.py          # Clase Historial para gestión de iteraciones
│   └── 📄 utils.py              # Evaluación de f(x), LaTeX, PDF y configuración
│
├── 📂 archivos/                 # Documentación PDF y consignas del TP
├── 📂 animaciones/              # Archivos JSON para animaciones Lottie
└── 📄 requirements.txt          # Dependencias del proyecto
```

## 🏗️ Arquitectura
Los métodos heredan de la clase abstracta `MetodoNumerico`, que define el esqueleto
común de toda la UI (`mostrar_info`). Cada subclase solo implementa lo que es único:
`render_inputs`, `ejecutar`, `render_teoria`, etc. Agregar un método nuevo = crear
un archivo y registrarlo en `app.py`.

## 🛠️ Tecnologías
Python · Streamlit · NumPy · Plotly · Pandas · SymPy · fpdf2 · Kaleido