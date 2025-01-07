from dash import html, dcc
import dash_bootstrap_components as dbc
from data import df
from styles import sidebar_style, content_style

def render_sidebar():
    return html.Div(
        id="sidebar",
        style=sidebar_style,
        children=[
            html.H4("Seleccionar Parámetros"),
            html.Label("Seleccionar Corregimiento"),
            dcc.Dropdown(
                id="dropdown-corregimiento",
                options=[{'label': c, 'value': c} for c in df["CORREGIMIENTO"].unique()],
                placeholder="Seleccione un corregimiento",
                clearable=False
            ),
            html.Br(),
            html.Label("Seleccionar Planta"),
            dcc.Dropdown(
                id="dropdown-planta",
                placeholder="Seleccione una planta",
                clearable=False
            ),
            html.Br(),
            html.Div(
                id="imagen-planta-container",
                style={'text-align': 'center', 'margin-top': '10px'},
                children=[
                    html.Img(id="imagen-planta", src="", style={'width': '100%', 'height': 'auto'})
                ]
            ),
            html.Div(
                id="navigation-buttons",
                style={'margin-top': '20px', 'display': 'none'},
                children=[
                    dbc.Button("Estadísticas", href="/estadistica", color="danger", className='me-2', style={'width': '100%'}),
                    html.Br(),
                    dbc.Button("Visualizaciones", href="/visualizacion", color="primary", style={'width': '100%', 'margin-top': '10px'}),
                    html.Br(),
                    dbc.Button("Detalles de Plantas", href="/detalles", color="info", style={"width": "100%", "marginTop": "10px"})
                ]
            )
        ]
    )
