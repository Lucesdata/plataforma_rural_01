from dash import Input, Output
import pandas as pd
import plotly.express as px
from data import get_sensor_data

def register_estadisticas_callbacks(app):
    @app.callback(
        Output("estadisticas-titulo", "children"),
        Output("estadisticas-grafico", "figure"),
        Input("dropdown-planta", "value")
    )
    def actualizar_estadisticas(planta):
        if planta:
            # Obtener los datos de la planta seleccionada
            datos = get_sensor_data(planta)
            if not datos.empty:
                titulo = f"Estadísticas de {planta}"
                figura = px.bar(datos, x="Fecha", y=datos.columns[1:], title=titulo)
                return titulo, figura
            else:
                return f"No hay datos disponibles para {planta}", px.bar(title="Sin datos")
        return "Seleccione una planta para ver las estadísticas", px.bar(title="Sin datos seleccionados")

