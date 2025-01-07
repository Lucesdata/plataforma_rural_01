from dash import Input, Output, html
import dash_bootstrap_components as dbc
from data import df
from pages.informacion_general import informacion_general_layout

def register_home_callbacks(app):
    # Callback para actualizar el dropdown de plantas
    @app.callback(
        Output("dropdown-planta", "options"),
        Input("dropdown-corregimiento", "value")
    )
    def actualizar_dropdown_plantas(corregimiento):
        if corregimiento:
            plantas = df[df["CORREGIMIENTO"] == corregimiento]["PLANTA"].unique()
            return [{'label': planta, 'value': planta} for planta in plantas]
        return []

    # Callback para actualizar la imagen de la planta
    @app.callback(
        Output("imagen-planta", "src"),
        Input("dropdown-planta", "value")
    )
    def actualizar_imagen_planta(planta):
        if planta:
            imagen = df.loc[df["PLANTA"] == planta, "IMAGEN"].values[0]
            return imagen
        return ""

    # Callback para mostrar/ocultar los botones de navegación
    @app.callback(
        Output("navigation-buttons", "children"),
        Input("dropdown-planta", "value")
    )
    def mostrar_botones(planta):
        if planta:
            return [
                dbc.Button("Estadísticas", href="/estadisticas", color="danger", className='me-2', style={'display': 'inline-block'}),
                dbc.Button("Visualizaciones", href="/visualizaciones", color="primary", style={'display': 'inline-block'})
            ]
        return [
            dbc.Button("Estadísticas", href="/estadisticas", color="danger", className='me-2', style={'display': 'none'}),
            dbc.Button("Visualizaciones", href="/visualizaciones", color="primary", style={'display': 'none'})
        ]

    # Callback para actualizar la información dinámica en el contenedor central
    @app.callback(
        Output("content-container", "children"),
        Input("dropdown-planta", "value")
    )
    def actualizar_informacion_planta(planta):
        if planta:
            datos = df[df["PLANTA"] == planta]
            return html.Div([
                html.H3(f"Información de {planta}", style={'text-align': 'center'}),
                html.Ul([
                    html.Li(f"Nombre: {datos['NOMBRE'].values[0]}"),
                    html.Li(f"Vereda: {datos['VEREDA'].values[0]}"),
                    html.Li(f"Corregimiento: {datos['CORREGIMIENTO'].values[0]}"),
                    html.Li(f"Fuente: {datos['FUENTE'].values[0]}")
                ])
            ])
        return informacion_general_layout()

    # Callback para actualizar los detalles de la planta
    @app.callback(
        Output("planta-detalles", "children"),  # Contenedor donde se mostrarán los detalles
        Input("dropdown-planta", "value")  # Valor seleccionado en el dropdown
    )
    def actualizar_detalles_planta(planta):
        if not planta:
            return html.P("Seleccione una planta para ver los detalles.", style={"textAlign": "center"})

        # Buscar los detalles de la planta seleccionada
        detalles = df[df["PLANTA"] == planta].iloc[0]
        
        # Crear el layout dinámico con los detalles de la planta
        return html.Div([
            html.H3(f"Detalles de {planta}", style={"textAlign": "center", "marginBottom": "20px"}),
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
        ])
