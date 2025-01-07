from dash import Input, Output
import pandas as pd
import plotly.express as px
from data import get_sensor_data

def register_visualizaciones_callbacks(app):
    @app.callback(
        Output("visualizaciones-titulo", "children"),
        Output("visualizaciones-grafico", "figure"),
        Input("dropdown-planta", "value")
    )
    def actualizar_visualizaciones(planta):
        if planta:
            # Obtener los datos de la planta seleccionada
            datos = get_sensor_data(planta)
            if not datos.empty:
                titulo = f"Visualizaciones de {planta}"
                figura = px.line(datos, x="Fecha", y=datos.columns[1:], title=titulo, markers=True)
                return titulo, figura
            else:
                return f"No hay datos disponibles para {planta}", px.line(title="Sin datos")
        return "Seleccione una planta para ver las visualizaciones", px.line(title="Sin datos seleccionados")
