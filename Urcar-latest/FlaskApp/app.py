import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from views import add, query, show, trade
from views import pageD


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

welcome = dbc.Container(
    [
        html.H1(
            'Welcome',
            className="display-1 ",
            style={
                'margin-left': '-15px',
            }
        ),
        html.Br(),
        html.Hr(),
    ],
    style={
        'margin-top': '180px',
        'max-width': '400px',
    }
)

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=True),

        dcc.Link('SHOW', href='/show', refresh=True, style={'margin-left': '0px'}),

        dcc.Link('ADD', href='/add', refresh=True, style={'margin-left': '40px'}),

        dcc.Link('QUERY', href='/query', refresh=True, style={'margin-left': '40px'}),

        dcc.Link('TRADE', href='/trade', refresh=True, style={'margin-left': '40px'}),

        # dcc.Link('pageD', href='/pageD', refresh=True, style={'margin-left': '40px'}),

        html.Hr(),  # 分隔线

        html.Div(id='render-page-content'),

    ],
    style={
        'paddingTop': '20px'
    }
)


@callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return welcome

    elif pathname == '/show':
        return show.layout

    elif pathname == '/add':
        return add.layout

    elif pathname == '/query':
        return query.layout

    elif pathname == '/trade':
        return trade.layout

    elif pathname == '/pageD':
        return pageD.layout

    else:
        return '404 NOT FOUND'


if __name__ == '__main__':
    app.run_server(debug=False)
