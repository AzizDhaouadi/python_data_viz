import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app



layout = html.Div(style={'margin-top':'1%'}, children=[
    html.Ul(children=[
        html.Li( style={'display': 'inline-block'},children=[
            html.A('Google Analytics Reports', href='dashboard/google_analytics', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]
        ),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('Google Ads Reports', href='dashboard/google_ads', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ])
    ], style={'list-style-type': 'none'}),

],className='container')

# layout = import init





 