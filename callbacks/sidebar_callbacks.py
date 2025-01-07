from dash import Input, Output
from data import df

def register_sidebar_callbacks(app):
    @app.callback(
        Output("dropdown-planta", "options"),
        Input("dropdown-corregimiento", "value")
    )
    def actualizar_dropdown_plantas(corregimiento):
        if corregimiento:
            plantas = df[df["CORREGIMIENTO"] == corregimiento]["PLANTA"].unique()
            return [{'label': planta, 'value': planta} for planta in plantas]
        return []

    @app.callback(
        Output("imagen-planta", "src"),
        Output("navigation-buttons", "style"),
        Output("selected-planta", "data"),  # Combina ambos outputs en este callback
        Input("dropdown-planta", "value")
    )
    def actualizar_imagen_y_toggle_botones(planta):
        if planta:
            imagen = df.loc[df["PLANTA"] == planta, "IMAGEN"].values[0]
            return (
                imagen,
                {'margin-top': '20px', 'display': 'block'},  # Mostrar los botones
                planta  # Actualizar el Store
            )
        return (
            "",  # Imagen vacía
            {'margin-top': '20px', 'display': 'none'},  # Ocultar los botones
            None  # Resetear el Store
        )

