import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import numpy as np

from app import app


df_sem_nine = pd.read_csv('data/SEM-OCT-CR.csv', index_col=0, parse_dates=True)
df_sem_nine.index = pd.to_datetime(df_sem_nine['Date'])

df_sem_ten = pd.read_csv('data/SEM-OCT-CTR.csv', index_col=0, parse_dates=True)
df_sem_ten.index = pd.to_datetime(df_sem_ten['Date'])

df_sem_el = pd.read_csv('data/SEM-OCT-IMP.csv', index_col=0, parse_dates=True)
df_sem_el.index = pd.to_datetime(df_sem_el['Date'])

# Creating a list of Dictionaries for label and value keys
def get_options(list_options):
    dic_list = []
    for i in list_options:
        dic_list.append({'label': i, 'value': i})

    return dic_list


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
            html.A('Other Marketing Reports', href='/dashboard/marketing_tools', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]),
    ], style={'list-style-type': 'none'}),


    ]),

    html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                          children=[
                              html.H1('Key Performance Indicators'),
                              html.H2('Campaigns Conversion Rate', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '2em'}),
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='sem_adconversion',
                                                        options=get_options(df_sem_nine['Conversion Rate'].unique()),
                                                          multi=True,
                                                        value=[df_sem_nine['Conversion Rate'].sort_values()[0]],
                                                        style={'backgroundColor': '#1E1E1E'},
                                                        className='adconversion')
                                       ],
                                       style={'color': '#1E1E1E'}),   

                              html.H2('Campaigns Click-Through Rate', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='sem_adctr',
                                                        options=get_options(df_sem_ten['CTR'].unique()),
                                                          multi=True,
                                                        value=[df_sem_ten['CTR'].sort_values()[0]],
                                                        style={'backgroundColor': '#1E1E1E'},
                                                        className='adctr')
                                       ],
                                       style={'color': '#1E1E1E'}),

                              html.H2('Campaigns Impressions', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '18em'}),
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='sem_adimpression',
                                                        options=get_options(df_sem_el['Impressions'].unique()),
                                                          multi=True,
                                                        value=[df_sem_el['Impressions'].sort_values()[0]],
                                                        style={'backgroundColor': '#1E1E1E'},
                                                        className='adimpression')
                                       ],
                                       style={'color': '#1E1E1E'}),               
               
  
                          ]
                          ),
                          
                html.Div(className=' eight columns div-for-charts bg-grey',
                          children=[
                    
                                dcc.Graph(id='sem_ads', config={'displayModeBar': False}), #Ad Covnversion Rate Graph
                                html.Br(), 
                                

                                dcc.Graph(id='sem_ctr', config={'displayModeBar': False}), #Ad Click-Through Rate Graph
                                html.Br(), 
 

                                dcc.Graph(id='sem_imp', config={'displayModeBar': False}), #Ad Impressions Graph
                                html.Br(), 
                                 
                          ])
             ])
])


# Update Ad Conversions
@app.callback(Output('sem_ads', 'figure'),
                      [Input('sem_adconversion', 'value')])
                      
def update_conversions(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_sem_nine = df_sem_nine
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_sem_nine[df_sub_sem_nine['Conversion Rate'] == stock].index,
                                y=df_sub_sem_nine[df_sub_sem_nine['Conversion Rate'] == stock]['value'],
                                mode='lines',
                                opacity=0.7,
                                name=stock,
                                textposition='bottom center'))
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  xaxis={'range': [df_sub_sem_nine.index.min(), df_sub_sem_nine.index.max()], 'showgrid':False},
                  yaxis={'showgrid':False}
              ),

              }

    return figure

# Update Ad Click-Through Rate
@app.callback(Output('sem_ctr', 'figure'),
                      [Input('sem_adctr', 'value')])
                      
def update_ctr(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_sem_ten = df_sem_ten
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_sem_ten[df_sub_sem_ten['CTR'] == stock].index,
                                y=df_sub_sem_ten[df_sub_sem_ten['CTR'] == stock]['value'],
                                mode='markers',
                                opacity=0.7,
                                name=stock,
                                textposition='bottom center'))
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=['#ffffff', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  xaxis={'range': [df_sub_sem_ten.index.min(), df_sub_sem_ten.index.max()], 'showgrid':False},
                  yaxis={'showgrid':False}
              ),

              }

    return figure

# Update Ad Click-Through Rate
@app.callback(Output('sem_imp', 'figure'),
                      [Input('sem_adimpression', 'value')])
                      
def update_ctr(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_sem_el = df_sem_el
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_sem_el[df_sub_sem_el['Impressions'] == stock].index,
                                y=df_sub_sem_el[df_sub_sem_el['Impressions'] == stock]['value'],
                                mode='lines',
                                opacity=0.7,
                                name=stock,
                                textposition='bottom center'))
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  xaxis={'range': [df_sub_sem_el.index.min(), df_sub_sem_el.index.max()],'showgrid':False},
                  yaxis={'showgrid':False}
              ),

              }

    return figure

