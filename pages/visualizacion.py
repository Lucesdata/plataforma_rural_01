from dash import html, dcc
import plotly.express as px

def visualizacion_layout():
    return html.Div([
        html.H2(id="visualizaciones-titulo", style={'text-align': 'center'}),
        dcc.Graph(id="visualizaciones-grafico"),
        html.Div(
            style={'text-align': 'center', 'margin-top': '20px'},
            children=[
                html.A("Volver al Home", href="/", style={'color': 'blue', 'font-size': '18px'})
            ]
        )
    ])

