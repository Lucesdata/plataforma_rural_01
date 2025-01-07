from dash import html
import dash_bootstrap_components as dbc
from data import df

def detalles_planta_layout(planta):
    # Obtener los detalles de la planta seleccionada
    detalles = df[df["PLANTA"] == planta].iloc[0]

    # Layout dinámico para mostrar los detalles de la planta
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H2(f"Detalles de {planta}", style={"text-align": "center", "margin-bottom": "20px"}),
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
            )
        ]
    )
