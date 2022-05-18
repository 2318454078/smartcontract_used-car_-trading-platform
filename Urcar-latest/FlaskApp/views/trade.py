# https://www.cnblogs.com/feffery/tag/Dash/
import json
import time
import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State, ALL
from web3 import Web3
from web3 import Web3,HTTPProvider,IPCProvider,WebsocketProvider
from dash.exceptions import PreventUpdate

w3 = Web3(Web3.EthereumTesterProvider())
# w3=Web3(HTTPProvider('HTTP://127.0.0.1:7545'))
fromAddress = w3.eth.accounts[0] #买车的人
toAddress = w3.eth.accounts[1] #车主，收款人地址


layout = html.Div(
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

            html.Br(),

            dbc.Container(
                    html.H1('Trade Cars',className="display-4 "),
                    style={
                        'max-width': '310px'
                    }
                ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col("Your account address:",className="lead"),
                    dbc.Col(dbc.Label(fromAddress),className="lead"),
                ]
            ),
            html.Hr(),
            html.H3('Please select the car you want to purchase'),
            dcc.Dropdown(id="input1",
                options=[
                    {'label': 'BMJSER_alfa-romero giulia', 'value': 13495},
                    {'label': 'YEORFT_audi 100 ls', 'value': 13950},
                    {'label': 'FWIBH1_bmw 320i', 'value': 16430},
                    {'label': 'KWMFOR_chevrolet impala', 'value': 5151},
                    {'label': 'L3YIVX_dodge rampage', 'value': 5572},
                    {'label': 'VO35Q7_honda civic', 'value': 6479},
                    {'label': 'KAS1Q7_isuzu MU-X', 'value': 6785},
                    {'label': 'ST9XPG_jaguar xj', 'value': 32250},
                    {'label': 'JOMZA0_maxda rx3', 'value': 5195},
                ],
                    placeholder='Please choose：'),

            html.Hr(),
            dbc.Row(
                [
                    dbc.Col("Owner account address:",className="lead"),
                    dbc.Col(dbc.Label(id='output1'),className="lead"),
                ]
            ),

            html.Hr(),
            dbc.Row(
                [
                    dbc.Col("Price of the car:",className="lead"),
                    dbc.Col(dbc.Label(id='output2'),className="lead"),
                ]
            ),

            html.Hr(),
        
            dbc.Container(
                html.Div(
                    [
                        dbc.Button(' Trade ', id='account-submit',color="primary",className="d-grid gap-4 col-4 ",style={'margin-left': '180px',}), 
                        html.A(html.Button('Refresh Data'),href='/trade',style={'margin-left': '40px',}),
                        dbc.Spinner(html.Div(id="loading-output",style={'margin-top': '30px',})),
                    ],
                    
                    # className="d-grid gap-1 col-2 mx-auto",
                ),
                style={
                    'max-width': '600px'
                }
            ),
            html.Br(),
            html.Br(),
            html.Div(id='account-record-container',),
        ],
        style={
            'margin-top': '20px',
            'max-width': '800px'
            }
    )

)

@callback(
    Output('output1', 'children'),
    Output('output2', 'children'),
    Input('input1', 'value'),
    prevent_initial_call=True
)
def callback1(value):
    global price
    global address_car_owner
    address_car_owner = 0
    if value == 13495:
        price = value
        address_car_owner = w3.eth.accounts[1]
        return address_car_owner,(str(price)+" wei")
    elif  value == 13950:
        price = value
        address_car_owner = w3.eth.accounts[2]
        return address_car_owner,(str(price)+" wei")
    elif  value == 16430:
        price = value
        address_car_owner = w3.eth.accounts[3]
        return address_car_owner,(str(price)+" wei")
    elif  value == 5151:
        price = value
        address_car_owner = w3.eth.accounts[4]
        return address_car_owner,(str(price)+" wei")
    elif  value == 5572:
        price = value
        address_car_owner = w3.eth.accounts[5]
        return address_car_owner,(str(price)+" wei")
    elif  value == 6479:
        price = value
        address_car_owner = w3.eth.accounts[6]
        return address_car_owner,(str(price)+" wei")
    elif  value == 6785:
        price = value
        address_car_owner = w3.eth.accounts[7]
        return address_car_owner,(str(price)+" wei")
    elif  value == 32250:
        price = value
        address_car_owner = w3.eth.accounts[8]
        return address_car_owner,(str(price)+" wei")
    elif  value == 5195:
        price = value
        address_car_owner = w3.eth.accounts[9]
        return address_car_owner,(str(price)+" wei")
    else:
        return ""

@callback(
    Output('account-record-container', 'children'),
    Output("loading-output", "children"),
    Input('account-submit', 'n_clicks'),
    Input('input1','value'),
    prevent_initial_call=True
)
def callback2(n_clicks,value_car):
    global address_car_owner
    global fromAddress
    if value_car != None:
        if n_clicks :
        # 发起交易
            time.sleep(1)
            trans = w3.eth.send_transaction({
                'to': address_car_owner,
                'from': fromAddress,
                'value': value_car
            })
            trans_hash = w3.eth.get_transaction(trans)
            address_car_owner = fromAddress
            trans_hash = dict(trans_hash)
            ctx_msg = json.dumps({
                'hash': str(trans_hash["hash"].hex()),
                'blockHash': str(trans_hash["blockHash"].hex()),
                'nonce': trans_hash["nonce"],
                'blockNumber':trans_hash["blockNumber"],
                'transactionIndex':trans_hash['transactionIndex'],
                'from':trans_hash['from'],
                'to':trans_hash['to'],
                'value':trans_hash['value'],
                'gas':trans_hash["gas"],
                "gasPrice":trans_hash["gasPrice"]
            }, indent=2)
# dbc.Alert("Has been traded to "+str(address_car_owner)+"\n"+"Congratulations! The deal was successful!", color="success" ,style={
#                 'margin-top': '10px',
#                 })
            return [html.Pre(ctx_msg),dbc.Alert(
    [
        html.H4("Congratulations! The deal was successful!", className="alert-heading"),
        html.Hr(),
        html.P(
            "Car has been traded to "+str(address_car_owner),
            className="mb-0",
        ),
    ]
)]
        else :
            raise PreventUpdate
    else:
        if n_clicks :
            n_clicks = 0
            return "",dbc.Alert("Please select a car", color="danger")
        else:
            raise PreventUpdate
            