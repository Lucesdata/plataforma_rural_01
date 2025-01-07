from dash import html, dcc
import dash_bootstrap_components as dbc
from components.overview_2020 import overview_2020_layout
from components.overview_2023 import overview_2023_layout  # Asegúrate de que este archivo exista

def informacion_general_layout():
    return html.Div([
        # Título principal con estilo actualizado
        html.H1(
            [
                "Monitoreo y Automatización de ",
                html.Span(
                    [
                        "PTAP'S",
                        dbc.Badge(
                            "10",
                            color="danger",
                            text_color="light",
                            className="ms-1",
                            style={
                                "fontSize": "18px",  # Tamaño más pequeño para el badge
                                "position": "relative",  # Posición relativa
                                "top": "-10px",  # Elevar el badge
                                "marginLeft": "5px",  # Espaciado entre PTAP y el número
                                "border": "1px solid #dc3545",  # Borde del mismo color que el fondo
                                "borderRadius": "5px",  # Bordes redondeados
                                "backgroundColor": "#dc3545",  # Color sólido para el badge
                                "padding": "2px 6px"  # Espaciado interno del badge
                            }
                        ),
                    ],
                    style={
                        "fontSize": "40px",  # Tamaño grande para PTAP (igual al título)
                        "fontWeight": "bold",
                        "color": "#0056b3"  # Color consistente
                    }
                )
            ],
            style={"textAlign": "center", "marginBottom": "20px"}
        ),

        # Tabs para seleccionar el año
        dcc.Tabs(id="tabs", value="2020", children=[
            # Tab para el año 2020
            dcc.Tab(label="Proyecto 2020", value="2020", children=[
                overview_2020_layout()  # Llama al layout de 2020
            ]),

            # Tab para el año 2023
            dcc.Tab(label="Proyecto 2023", value="2023", children=[
                overview_2023_layout()  # Llama al layout de 2023
            ]),
        ], style={'margin': '10px'})
    ])