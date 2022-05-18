import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, callback
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        dcc.Location(id='url_pageD'),

        html.Hr(),

        dcc.Link('query', href='/query', refresh=True, style={'margin-left': '40px'}),

        dcc.Link('add', href='/add', refresh=True, style={'margin-left': '40px'}),

        html.Hr(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Which page : ', html_for='input_page'),
                        dcc.Dropdown(
                            id='input_page',
                            options=[
                                {"label": "query", "value": "query"},
                                {"label": "add", "value": "add"},
                            ],
                        ),
                    ],
                ),
            ],
        ),

        html.Hr(),

        dbc.Container(
            [
                dbc.Button(
                    'Jump',
                    id='jump-button',
                    size='lg',
                    color="primary",
                    className="d-grid gap-4 col-12 ",
                ),
            ],
            style={
                'max-width': '300px'
            }
        ),

    ],
    style={
        'paddingTop': '100px'
    }
)


@callback(
    Output('url_pageD', 'pathname'),
    Input('jump-button', 'n_clicks'),
    State('input_page', 'value'),
    prevent_initial_call=True,
)
def render_page_content(n_clicks, page_name):

    if n_clicks:
        if page_name=='query':
            return '/query'
        
        elif page_name=='add':
            return '/add'
        
    return dash.no_update

