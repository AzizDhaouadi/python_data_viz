import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div(style={'margin-top':'1%'}, children=[
    html.Ul(children=[
        html.Li( style={'display': 'inline-block', 'margin-left': '100px'},children=[
            html.A('Primary Reports', href='apps/app1', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]
        ),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('SEM Reports', href='apps/app2', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ])
    ], style={'list-style-type': 'none'}),

    html.Hr(style={'display': 'block', 'height': '1px',
        'border': '0', 'border-top': '1px solid #828282',
        'margin': '6em 0', 'padding': '0'}),

    html.Div(children=[
    html.Div(className='row',
    children=[
        html.Div(className='four columns div-for-charts bg-grey',
            children=[
                html.P('Welcome to the TrafficJunky Marketing Dashboard !', style = {
                    'margin-top': '-4em'
                })
                 
            ]
        ),
        html.Div(className='eight columns div-for-charts bg-grey',
            children=[
                html.P('Choose the Reports you want to consult in the Header Menu', style = {
                    'margin-top': '-4em'
                })
                 
            ])
    ])
]),
    
    html.Hr(style={'display': 'block', 'height': '1px','border': '0', 'border-top': '1px solid #828282','margin': '6em 0', 'padding': '0'}),
    
    html.Div(children=[
    html.Div(className='row',
    children=[
        html.Div(className='four columns div-user-controls bg-grey',
            children=[
                html.P('This Dashboard is dedicated to the Marketing & PO team. It is maintained by the Marketing team, which holds the right to change the content without notice.', style = {
                    'margin-top': '-7em'
                })
                 
            ]
        ),
        html.Div(className='eight columns div-user-controls bg-grey',
            children=[
                html.P('For questions, comments, change requests or just to say hi, please contact chiara.ferrero@mindgeek.com', style = {
                    'margin-top': '-7em', 'margin-left': '2em'
                })
                 
            ])
    ])
]),

],className='container')






 