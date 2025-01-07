from dash import Input, Output, State
import dash_bootstrap_components as dbc


#2023

def register_modals_callbacks(app):
    @app.callback(
        Output("info-modal", "is_open"),
        [Input("open-info-modal", "n_clicks"), Input("close-info-modal", "n_clicks")],
        [State("info-modal", "is_open")],
    )
    def toggle_info_modal(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open

    @app.callback(
        Output("objetivos-modal", "is_open"),
        [Input("open-objetivos-modal", "n_clicks"), Input("close-objetivos-modal", "n_clicks")],
        [State("objetivos-modal", "is_open")],
    )
    def toggle_objetivos_modal(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open

    @app.callback(
        Output("plantas-modal", "is_open"),
        [Input("open-plantas-modal", "n_clicks"), Input("close-plantas-modal", "n_clicks")],
        [State("plantas-modal", "is_open")],
    )
    def toggle_plantas_modal(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open

    
#2020

def register_modals_callbacks2(app):
    @app.callback(
        Output("info-modal2", "is_open"),
        [Input("open-info-modal2", "n_clicks"), Input("close-info-modal2", "n_clicks")],
        [State("info-modal2", "is_open")],
    )
    def toggle_info_modal2(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open
    
    @app.callback(
        Output("objetivos-modal2", "is_open"),
        [Input("open-objetivos-modal2", "n_clicks"), Input("close-objetivos-modal2", "n_clicks")],
        [State("objetivos-modal2", "is_open")],
    )
    def toggle_objetivos_modal2(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open
    
    @app.callback(
        Output("plantas-modal2", "is_open"),
        [Input("open-plantas-modal2", "n_clicks"), Input("close-plantas-modal2", "n_clicks")],
        [State("plantas-modal2", "is_open")],
    )
    def toggle_plantas_modal(open_click, close_click, is_open):
        if open_click or close_click:
            return not is_open
        return is_open