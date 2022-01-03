import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
from app import app
import numpy as np

# Defining the Layout of the App
layout = html.Div(children=[
    html.Div(style={'margin-top':'1%'}, children=[
    html.Ul(children=[
        html.Li( style={'display': 'inline-block', 'margin-left': '100px'},children=[
            html.A('Home', href='/', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]
        ),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('Google Analytics Reports', href='/dashboard/google_analytics', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('Google Ads Reports', href='/dashboard/google_ads', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('Other Marketing Reports', href='/dashboard/marketing_tools', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]),
    ], style={'list-style-type': 'none'}),


    ]),

    html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                          children=[
                              html.H2('Ad Groups Conversion Breakdown', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '2em'}),
                              html.H2('Conversions By Campaign', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '21em'}),
                              html.H2('Clicks vs Conversions', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '21em'}),
                              html.H2('Conversions vs Revenue', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '21em'}),
                              
                          ]
                          ),
                          
                html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id='event_spend', config={'displayModeBar': False}),
                                html.Br(),
                                dcc.Graph(id='campaigns', config={'displayModeBar': False}),
                                html.Br(),
                                dcc.Graph(id='conversions', config={'displayModeBar': False}),
                                html.Br(),
                                dcc.Graph(id='revenue', config={'displayModeBar': False}),
                                html.Br()
                                 
                          ])
             ])
])


@app.callback(Output('event_spend', 'figure'),[Input('event_spend', 'value')])                
def update_eventspend(selected_dropdown_value):
    trace = go.Pie(labels = ['Ad Group 1', 'Ad Group 2', 'Ad Group 3', 'Ad Group 4', 'Ad Group 5'], values=[23,17,35,29,12])
    data = [trace]
    # Define Figure
    # STEP 4
    figure = {
        'data': data,
        'layout': go.Layout(
            colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
            template='plotly_dark',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            margin={'b': 15},
            hovermode='x',
            autosize=True,
        )
    }

    return figure

@app.callback(Output('campaigns', 'figure'),[Input('campaigns', 'value')])                
def update_campaigns(selected_dropdown_value):
    campaigns = ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D', 'Campaign E']
    conversions = [23,17,35,29,12]
    data = [go.Bar(
        x = campaigns,
        y = conversions
        )]                                
    
    figure = {
        'data': data,
        'layout': go.Layout(
            colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
            template='plotly_dark',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            margin={'b': 15},
            hovermode='x',
            autosize=True,
        )
    }

    return figure

@app.callback(Output('conversions', 'figure'),[Input('conversions', 'value')])                
def update_eventspend(selected_dropdown_value):
    trace = go.Scatter(x = ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4', 'Campaign 5'], y=[23,17,35,29,12], stackgroup='one', name='convesions')
    trace_two = go.Scatter(x = ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4', 'Campaign 5'], y=[43,27,55,69,42], stackgroup='one', name='clicks')

    # STEP 3

    data = [trace,trace_two]
    # Define Figure
    # STEP 4
    figure = {
        'data': data,
        'layout': go.Layout(
            colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
            template='plotly_dark',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            margin={'b': 15},
            hovermode='x',
            autosize=True,
        )
    }

    return figure

@app.callback(Output('revenue', 'figure'),[Input('revenue', 'value')])                
def update_eventspend(selected_dropdown_value):
    data = go.Bar(x = ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4', 'Campaign 5'], y=[23,17,35,29,12], name='conversions')
    trace = go.Scatter(x = ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4', 'Campaign 5'], y=[43,27,55,69,42], mode='markers', name="revenue")

    # STEP 3

    datas = [data,trace]
    # Define Figure
    # STEP 4
    figure = {
        'data': datas,
        'layout': go.Layout(
            colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
            template='plotly_dark',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            margin={'b': 15},
            hovermode='x',
            autosize=True
        )
    }

    return figure