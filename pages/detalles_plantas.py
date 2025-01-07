from dash import html
import dash_bootstrap_components as dbc
from data import df

def detalles_planta_layout(planta):
    if not planta:
        return html.Div(
            style={"textAlign": "center"},
            children=html.P("Seleccione una planta para ver los detalles.")
        )

    detalles = df[df["PLANTA"] == planta].iloc[0]

    return html.Div(
        style={"padding": "20px", "max-width": "1200px", "margin": "0 auto"},
        children=[
            html.H2(f"Detalles de la Planta: {planta}", style={"textAlign": "center", "marginBottom": "20px"}),
            dbc.Card(
                dbc.CardBody([
                    html.Ul([
                        html.Li(f"Nombre: {detalles['NOMBRE']}"),
                        html.Li(f"Vereda: {detalles['VEREDA']}"),
                        html.Li(f"Corregimiento: {detalles['CORREGIMIENTO']}"),
                        html.Li(f"Fuente: {detalles['FUENTE']}"),
                        html.Li(f"Caudal Diseño: {detalles['CAUDAL DISEÑO']} L/s"),
                        html.Li(f"Caudal Concesión: {detalles['CAUDAL CONCESION']} L/s"),
                        html.Li(f"Tipo de Planta: {detalles['TIPO DE PLANTA']}"),
                        html.Li(f"Usuarios: {detalles['Usuarios']}"),
                        html.Li(f"Población: {detalles['Población']}"),
                        html.Li(f"Ubicación: {detalles['LATITUD']}, {detalles['LONGITUD']}"),
                    ])
                ]),
                className="shadow-sm mb-3"
            ),
            # Botón para volver al Home
            html.Div(
                style={"textAlign": "center", "marginTop": "20px"},
                children=[
                    dbc.Button("Volver al Home", href="/", color="primary", className="btn-lg")
                ]
            )
        ]
    )

