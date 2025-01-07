from dash import html, dcc
import dash_bootstrap_components as dbc

def estadisticas_layout():
    return html.Div(
        style={'padding': '20px', 'max-width': '1200px', 'margin': '0 auto'},
        children=[
            html.H2(
                id="estadisticas-titulo",
                style={'text-align': 'center', 'margin-bottom': '20px', 'color': '#0056b3'}
            ),
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id="estadisticas-grafico")
                ]),
                className="shadow-sm"
            ),
            html.Div(
                style={'text-align': 'center', 'margin-top': '20px'},
                children=[
                    dbc.Button("Volver al Home", href="/", color="primary", className="me-2")
                ]
            )
        ]
    )


