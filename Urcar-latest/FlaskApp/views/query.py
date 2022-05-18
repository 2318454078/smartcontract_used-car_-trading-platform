import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
from init import tool
import time

layout = html.Div(
    [
        html.Br(),

        dbc.Container(
            [
                dbc.Container(
                    html.Img(
                        src='assets/fox.jpg',
                        style={
                            'width': '100%',
                            'height': '100%',
                            'margin-left': '-10px',
                            }
                    ),
                    style={
                        'max-width': '400px',
                    }
                ),

                # html.Hr(),  # 分割线

                dbc.Container(
                    html.H1(' Check Cars',className="display-4 "),
                    style={
                        'max-width': '330px'
                    }
                ),

                html.Hr(),  # 分割线

                # 车辆选择控件
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label('Car ID :'),
                                dbc.Input(type="text", id='input-queryID'),
                            ]
                        )
                    ]
                ),

                html.Br(),  # 空格

                # 查看内容选择控件
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label('Search : ', html_for='input_attributes'),
                                dcc.Dropdown(
                                    id='input_attributes',
                                    multi=True,
                                    options=[
                                        {'label': item, 'value': item}
                                        for item in ['Initial Info', 'Repair Info']
                                    ])
                            ],
                        )
                    ]
                ),

                html.Hr(),

                # 提交查询按钮

                dbc.Container(
                    [
                        dbc.Button(
                            'Query',
                            id='query-button',
                            size='lg',
                            color="primary",
                            className="d-grid gap-4 col-12 ",
                        ),
                    ],
                    style={
                        'max-width': '300px'
                    }
                ),

                html.Hr(),
                dbc.Spinner(html.Div(id="loading-query")),

                dbc.Tabs(
                    id='output-value',
                    style={'margin-top': '20px'},
                )

            ],
            style={
            'margin-top': '-20px',
            'max-width': '800px'
            }
        ),

    ]
)

@callback(
    Output("loading-query", "children"),
    Output('output-value', 'children'),
    Input('query-button', 'n_clicks'),
    State('input-queryID', 'value'),
    State('input_attributes', 'value'),
    prevent_initial_call=True,
)
def render_content(n_clicks, car_id, car_attributes):
    '''
    根据用户控件输入结果，进行相应查询结果的渲染
    :param n_clicks: 查询按钮点击次数
    :param car_id: 已选择的车辆对应id
    :param car_attributes: 已选择要展示的内容范围
    :return:
    '''

    # 当按钮被新一轮点击后
    if n_clicks:

        time.sleep(0.5)

        # 当car_id与car_attributes不为空时
        if car_id and car_attributes:

            # 获取该车辆全部信息
            if car_id in tool.addresses.keys():
                info_alert = 'query success'

                car_info = tool.getInfo(tool.addresses[car_id][0])
                if len(tool.addresses[car_id]) > 1:
                    new_info = [tool.getInfo(tool.addresses[car_id][i]) for i in range(1, len(tool.addresses[car_id]))]

                # 初始化Tabs返回结果
                tabs = []
                if 'Initial Info' in car_attributes:
                    # 渲染Initial Info面板内容
                    tabs.append(
                        dbc.Tab(
                            html.Blockquote(
                                [
                                    html.Br(),
                                    html.H4('car id: '+car_id),
                                    html.P(json.dumps(car_info)),
                                    html.Br(),
                                ],
                                style={
                                    'background-color': 'rgba(211, 211, 211, 0.25)',
                                    'text-indent': '1rem'
                                }
                            ),
                            label='Initial Info',
                        ),
                    ),

                if 'Repair Info' in car_attributes:
                    # 渲染Repair Info面板内容
                    tabs.append(
                        dbc.Tab(
                        html.Blockquote(

                                [html.Br()] + \
                                ([html.P(json.dumps(item)) for item in new_info] if len(tool.addresses[car_id])>1 else [html.H4('None')]) + \
                                [html.Br()],

                                style={
                                    'background-color': 'rgba(211, 211, 211, 0.25)',
                                    'text-indent': '1rem'
                                },
                            ),
                            label='Repair Info',
                        ),
                    ),

                # 返回渲染结果
                return dbc.Alert(info_alert, color="success" ,style={'margin-top': '0px',}), tabs

            else:
                return dbc.Alert('Please input the correct car-id', color="danger" ,style={'margin-top': '0px',}), []

        else:
            return dbc.Alert('Please input car-id and select what to query', color="danger" ,style={'margin-top': '0px',}), []

    return dash.no_update
