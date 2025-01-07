from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_daq as daq

# Estilos para tarjetas y texto
card_style = {
    'backgroundColor': '#f9f9f9',
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.2)',
    'textAlign': 'center',
    'marginBottom': '20px'
}

# Estilo con imagen para el encabezado
card_style_with_image_header = {
    'backgroundImage': 'linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url("/assets/monitoreo.jpg")',
    'backgroundSize': 'cover',
    'backgroundPosition': 'center',
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.2)',
    'textAlign': 'center',
    'color': '#333333',
    'marginBottom': '20px'
}

# Estilos para tarjetas con imágenes adicionales
card_style_with_image2 = {
    **card_style,
    'backgroundImage': 'linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url("/assets/turbidimetro.jpeg")',
    'backgroundSize': 'cover',
    'color': '#333333'
}
card_style_with_image3 = {
    **card_style,
    'backgroundImage': 'linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url("/assets/display.jpeg")',
    'backgroundSize': 'cover',
    'color': '#333333'
}

text_style = {'color': '#333333', 'fontSize': '18px'}
header_style = {'color': '#0056b3', 'fontSize': '28px', 'marginBottom': '20px'}

# Layout del resumen del proyecto 2023
def overview_2023_layout():
    return html.Div(
        style={'padding': '20px'},
        children=[
            # Encabezado y descripción con imagen
            html.Div(
                style=card_style_with_image_header,
                children=[
                    html.H1(
                        [
                            "Transformando la Gestión del ",
                            dbc.Badge("Agua", color="primary", className="ms-1")
                        ],
                        style=header_style
                    ),
                    html.P(
                        "Monitoreo y Automatización en tiempo real.",
                        style=text_style
                    ),
                    # Botones y modales de información
                    html.Div([
                        dbc.Button("General", id="open-info-modal", style={'margin': '10px'}, n_clicks=0),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Información General")),
                                dbc.ModalBody(
                                    "La transformación de la gestión del agua en la zona rural de Cali tiene como base el fortalecimiento de las capacidades de conectividad y monitoreo. Este proyecto busca implementar tecnologías innovadoras que permitan la comunicación eficiente entre las plantas rurales y una central de control, asegurando una supervisión constante y centralizada para mejorar el servicio a las comunidades."
                                ),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-info-modal", className="ms-auto", n_clicks=0)
                                ),
                            ],
                            id="info-modal",
                            is_open=False
                        ),
                        dbc.Button("Objetivos", id="open-objetivos-modal", style={'margin': '10px'}, n_clicks=0),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Objetivos del Proyecto")),
                                dbc.ModalBody([
                                    html.P("Se plantearán las causas técnicas que justifican la aplicación de este proyecto en estos 4 apartados:", style=text_style),
                                    html.Ul([
                                        html.Li("Tipo de Tecnología: Las plantas de tratamiento de agua en la zona rural de Cali son infraestructuras diseñadas bajo el principio de filtración en múltiples etapas (FIME)."),
                                        html.Li("Causas: El proyecto surge ante la necesidad de garantizar la calidad y cantidad de agua en zonas rurales."),
                                        html.Li("Misión: Implementar soluciones tecnológicas sostenibles para un servicio de agua potable eficiente."),
                                        html.Li("Resultado: Logró reducir en un 40% los costos operativos y mejorar el monitoreo en tiempo real."),
                                    ])
                                ]),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-objetivos-modal", className="ms-auto", n_clicks=0)
                                ),
                            ],
                            id="objetivos-modal",
                            is_open=False
                        ),
                        dbc.Button("Plantas", id="open-plantas-modal", style={'margin': '10px'}, n_clicks=0),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Plantas Piloto")),
                                dbc.ModalBody(
                                    "Las plantas piloto seleccionadas (Soledad, Carbonero y La Sirena) representan ejemplos estratégicos de cómo el proyecto se implementará. Estas plantas serán el punto de partida para probar tecnologías de monitoreo, automatización y comunicación, estableciendo un modelo replicable para otras instalaciones rurales."
                                ),
                                dbc.ModalFooter(
                                    dbc.Button("Cerrar", id="close-plantas-modal", className="ms-auto", n_clicks=0)
                                ),
                            ],
                            id="plantas-modal",
                            is_open=False
                        ),
                    ])
                ]
            ),
            # Tarjetas con DAQ
            html.Div(
                style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '20px'},
                children=[
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("PTAP's", className="card-title"),
                            daq.LEDDisplay(
                                value="10",
                                color="#0074D9",
                                backgroundColor="#f9f9f9",
                                size=48
                            ),
                            html.P("Plantas Monitoreadas.", className="card-text"),
                        ]),
                        style=card_style_with_image_header  # Imagen actualizada
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("Sensores Instalados", className="card-title"),
                            daq.LEDDisplay(
                                value="27",
                                color="#0074D9",
                                backgroundColor="#f9f9f9",
                                size=48
                            ),
                            html.P("Sensores de Cantidad.", className="card-text"),
                        ]),
                        style=card_style_with_image2
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("Datos por Día", className="card-title"),
                            daq.LEDDisplay(
                                value="10000",
                                color="#0074D9",
                                backgroundColor="#f9f9f9",
                                size=48
                            ),
                            html.P("Datos de Caudal y Nivel.", className="card-text"),
                        ]),
                        style=card_style_with_image3
                    )
                ]
            ),
            # Botones debajo de las tarjetas
            html.Div(
                [
                    dbc.Button("Contrato / Avance", className="btn btn-primary btn-lg mx-2", style={'width': '550px'}),
                    dbc.Button("Entrega / Funcionamiento", className="btn btn-primary btn-lg mx-2", style={'width': '550px'}),
                ],
                className="d-flex justify-content-center",
                style={'marginTop': '20px'}
            )
        ]
    )

