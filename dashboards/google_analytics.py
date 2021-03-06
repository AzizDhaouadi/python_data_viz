
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

from app import app


# Loading the data for the App
df = pd.read_csv('data/pageviews.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

df_two = pd.read_csv('data/bounce.csv', index_col=0, parse_dates=True)
df_two.index = pd.to_datetime(df_two['Date'])

df_three = pd.read_csv('data/exit.csv',index_col=0, parse_dates=True)
df_three.index = pd.to_datetime(df_three['Date'])

df_four = pd.read_csv('data/eventcreation.csv', index_col=0, parse_dates=True)
df_four.index = pd.to_datetime(df_four['Date'])

df_nine = pd.read_csv('data/adsconversion.csv', index_col=0, parse_dates=True)
df_nine.index = pd.to_datetime(df_nine['Date'])

df_ten = pd.read_csv('data/adsctr.csv', index_col=0, parse_dates=True)
df_ten.index = pd.to_datetime(df_ten['Date'])

df_el = pd.read_csv('data/adimpressions.csv', index_col=0, parse_dates=True)
df_el.index = pd.to_datetime(df_el['Date'])
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
                              html.H1('Key Performance Indicators'),

                              #Drowdown Menu for the pageviews
                              html.H2('Pageviews', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '2em'}),  
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='pageview',
                                                        options=get_options(df['Page'].unique()),
                                                        multi=True,
                                                        value=[df['Page'].sort_values()[0]],
                                                        style={'backgroundColor': 'inherit'},
                                                        className='pageview')
                                       ],
                                       style={'color': '#1E1E1E'}),

                                #Dropdown for the Bounce rate
                                html.H2('Bounce Rate', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='bounceselector',
                                                          options=get_options(df_two['Bounce'].unique()),
                                                          multi=True,
                                                          value=[df_two['Bounce'].sort_values()[0]],
                                                          style={'backgroundColor': 'inherit'} ,
                                                          className='bounceselector')       
                                         ],
                                         style={'color': '#000'}),

                                #Dropdown for the Exit rate
                                html.H2('Exit Rate', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='exitselector',
                                                          options=get_options(df_three['Exit'].unique()),
                                                          multi=True,
                                                          value=[df_three['Exit'].sort_values()[0]],
                                                          style={'backgroundColor': 'inherit'},
                                                          className='exitselector')       
                                         ],
                                         style={'color': '#1E1E1E'}),

                                html.H2('Events Tracking', style={'color': '#bc5090', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='evenselector',
                                                          options=get_options(df_four['Event'].unique()),
                                                          multi=True,
                                                          value=[df_four['Event'].sort_values()[0]],
                                                          style={'backgroundColor': 'inherit'} ,
                                                          className='evenselector')       
                                         ],
                                         style={'color': '#1E1E1E'}),
                           

                          ]
                          ),
                          
                html.Div(className=' eight columns div-for-charts bg-grey',
                          children=[
                              dcc.Graph(id='timeseries', config={'displayModeBar': False}), #Pageviews Graph
                              html.Br(), 

                              dcc.Graph(id='change', config={'displayModeBar': False}), # Bounce Rate Graph
                              html.Br(),

                              dcc.Graph(id='exit_rate', config={'displayModeBar': False}), # Exit Rate Graph
                              html.Br(), 

                             dcc.Graph(id='event_tracking', config={'displayModeBar': False}),# Event Tracking Graph 
                             html.Br(),

                            #  dcc.Graph(id='event_spending', config={'displayModeBar': False}),# Event Tracking Graph 
                            #  html.Br()
                              
                              ])
             ]),
            



])

# Update Pageviews
@app.callback(Output('timeseries', 'figure'),
                      [Input('pageview', 'value')])
                      
def update_pageviews(selected_dropdown_value):
    # STEP 1
    trace = []
    df_sub = df
    # STEP 2
    for value in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['Page'] == value].index,
                                y=df_sub[df_sub['Page'] == value]['value'],
                                mode='lines',
                                opacity=1,
                                name=value,
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
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()], 'showgrid':False},
                  yaxis = {'showgrid':False}
              ),

              }
    return figure


# Update Bounce Rate
@app.callback(Output('change', 'figure'),
                      [Input('bounceselector', 'value')])
                      
def update_bouncerate(selected_dropdown_value):
    # STEP 1
    trace = []
    df_sub_two = df_two
    # STEP 2
    for value in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_two[df_sub_two['Bounce'] == value].index,
                                y=df_sub_two[df_sub_two['Bounce'] == value]['value'],
                                mode='lines',
                                opacity=1,
                                name=value,
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
                #   title={'text': 'Bounce Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_two.index.min(), df_sub_two.index.max()], 'showgrid': False},
                  yaxis = {'showgrid':False}
              ),

              }

    return figure

# Update Exit Rate
@app.callback(Output('exit_rate', 'figure'),
                      [Input('exitselector', 'value')])
                      
def update_exitrate(selected_dropdown_value):
    # STEP 1
    trace = []
    df_sub_three = df_three
    # STEP 2
    for value in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_three[df_sub_three['Exit'] == value].index,
                                y=df_sub_three[df_sub_three['Exit'] == value]['value'],
                                mode='lines',
                                opacity=1,
                                name=value,
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
                #   title={'text': 'Exit Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_three.index.min(), df_sub_three.index.max()], 'showgrid':False},
                  yaxis = {'showgrid':False}
              ),

              }

    return figure

# Update Events Tracking
@app.callback(Output('event_tracking', 'figure'),
                      [Input('evenselector', 'value')])
                      
def update_eventstracking(selected_dropdown_value):
    # STEP 1
    trace = []
    df_sub_four = df_four
    # STEP 2
    for value in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_four[df_sub_four['Event'] == value].index,
                                y=df_sub_four[df_sub_four['Event'] == value]['value'],
                                mode='markers',
                                opacity=1,
                                name=value,
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
                  xaxis={'range': [df_sub_four.index.min(), df_sub_four.index.max()], 'showgrid':False},
                  yaxis = {'showgrid':False}
              ),

              }

    return figure
