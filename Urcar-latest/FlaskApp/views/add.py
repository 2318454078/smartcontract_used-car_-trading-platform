import dash
from dash import Dash, dcc, html, callback
import dash_bootstrap_components as dbc
from init import tool
from dash.dependencies import Input, Output, State
import time

layout = html.Div(
    [
        html.Br(),  # 换行

        dbc.Container(
            [
                dbc.Container(
                html.Img(
                    src='assets/car.jpg',
                    style={
                        'width': '100%',
                        'height': '100%',
                        'margin-left': '0px',
                    }    
                ),
                style={
                    'max-width': '500px'
                }
            ),
                dbc.Container(
                    html.H1('Add Cars',className="display-4 "),
                    style={
                        'max-width': '270px'
                    }
                ),

                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('1. Your identity')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "Factory", "value": 1},
                                    {"label": "Shop", "value": 2},
                                    {"label": "Checker", "value": 3}
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('2. Type of record')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "Ex factory", "value": 1},
                                    {"label": "Repair", "value": 2},
                                    {"label": "Transaction", "value": 3},
                                    {"label": "Varify", "value": 4},
                                    {"label": "Destroy", "value": 5},
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('3. Need what')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Checklist(
                                options=[
                                    {"label": "initial", "value": 1},
                                    {"label": "price", "value": 2},
                                    {"label": "odograph", "value": 3},
                                    {"label": "score", "value": 4},
                                    {"label": "others", "value": 5}
                                ],
                                inline=True
                            ),
                        )
                    ]
                ),
                html.Hr(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Label('Car ID: ', html_for='input-carID'),
                                    dbc.Input(type="text", id='input-carID'),
                                ]
                            ),
                            width=6
                        ),
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Label('Content: ', html_for='input-content'),
                                    dbc.Input(type="text", id='input-content'),
                                ]
                            ),
                            width=6
                        ),
                        
                    ],
                ),

                html.Hr(),
                html.Br(),

                dbc.Container(
                    dbc.Button(
                        'ADD',
                        id='add-button',
                        size='lg',
                        color="primary",
                        className="d-grid gap-4 col-12 ",
                        # style={'margin-left': '260px',}
                    ),
                    style={
                        'max-width': '300px'
                    }
                ),

                html.Hr(),
                dbc.Spinner(html.Div(id="loading-add",style={'margin-top': '0px',})),
  

            ],
            style={
            'margin-top': '0px',
            'max-width': '800px'
            }
        )
    ]
)

@callback(
    Output("loading-add", "children"),
    Input('add-button', 'n_clicks'),
    State('input-carID', 'value'),
    State('input-content', 'value'),
    prevent_initial_call=True
)
def refresh_output(n_clicks, carID, content):

    if n_clicks:

        time.sleep(0.5)

        if carID:
            if content:
                address = tool.new(content)
                if carID not in tool.addresses.keys():
                    tool.addresses[carID] = [address]
                    res =  carID + ' add init info'
                else:
                    tool.addresses[carID].append(address)
                    res =  carID + ' add more info'

                return dbc.Alert(res, color="success" ,style={'margin-top': '0px',})
                
            else:
                res =  'Please input content'
        else:
            res =  'Please input Car ID'
        
        return dbc.Alert(res, color="danger" ,style={'margin-top': '0px',})

    return dash.no_update


