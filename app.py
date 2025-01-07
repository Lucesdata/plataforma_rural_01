from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.sidebar import render_sidebar
from pages.informacion_general import informacion_general_layout
from pages.estadisticas import estadisticas_layout
from pages.visualizacion import visualizacion_layout
from pages.detalles_plantas import detalles_planta_layout  # Importar la función
from callbacks.sidebar_callbacks import register_sidebar_callbacks
from callbacks.modals_callbacks import register_modals_callbacks
from callbacks.estadisticas_callbacks import register_estadisticas_callbacks
from callbacks.visualizaciones_callbacks import register_visualizaciones_callbacks
from styles import sidebar_style, content_style

# Inicialización de la aplicación
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url"),
    dcc.Store(id="selected-planta"),
    render_sidebar(),
    html.Div(id="page-content", style=content_style)
])

# Navegación entre páginas
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"), Input("selected-planta", "data")]
)
def display_page(pathname, selected_planta):
    if pathname == "/estadistica":
        return estadisticas_layout()
    elif pathname == "/visualizacion":
        return visualizacion_layout()
    elif pathname == "/detalles" and selected_planta:
        return detalles_planta_layout(selected_planta)  # Pasamos la planta seleccionada
    else:
        return informacion_general_layout()



# Registrar callbacks
register_sidebar_callbacks(app)
register_modals_callbacks(app)
register_estadisticas_callbacks(app)
register_visualizaciones_callbacks(app)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)

