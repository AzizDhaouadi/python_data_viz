import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

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
            html.A('Home', href='/apps/app1', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]
        ),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('Google Analytics Reports', href='/apps/app2', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]),
        html.Hr(style={'display': 'block', 'height': '1px',
                'border': '0', 'border-top': '1px solid #828282', 'padding': '0'}),
    ], style={'list-style-type': 'none'}),

    html.Hr(style={'display': 'block', 'height': '1px',
        'border': '0', 'border-top': '1px solid #828282',
        'margin': '6em 0', 'padding': '0'}),
    ]),

    html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                          children=[
                              #Introduction to the Marketing Dashboard
                            #   html.Img(src='/assets/tj_logo.svg', style={'height': '45px', 'paddingBottom': '40px'}),
                              html.H1('Marketing Dashboard', style={'color': '#67c5d7', 'fontWeight': 'bolder', 'fontSize': '40px', 'fontFamily': 'Roboto'}),
                              html.P('This section reports the performacen of the SEM Campaigns running on Google Search & Google Display Network'),

                              html.H3('This is the list of the KPIs you will be able to visualize for our Google Ads'),
                              html.Li('Conversion Rate Per Campaign', style={'color': '#D77967', 'fontSize': 'large'}),
                              html.Li('Click-through Rate Per Campaign', style={'color': '#D77967', 'fontSize': 'large'}),
                              html.Li('Ad Impressions Per Campaign', style={'color': '#D77967', 'fontSize': 'large'}),


                                html.H2('Ads Conversion Rate Dropdown Menu', style={'color':'#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder'}),  
                                html.P('This will allow you to visualize the conversion rate for our Google Ads. The ads are broken down per Geo location, and do not include the display ads'),  
                                
                                html.H2('Ads Click-Through Rate Dropdown Menu', style={'color':'#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder'}),
                                html.P('This will allow you to visualize the click-through rate for our Google Ads. The ads are broken down per Geo location, and do not include the display ads'),

                                html.H2('Ads Impression Dropdown Menu', style={'color':'#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder'}),
                                html.P('This will allow you to visualize the ad impressions of our Goodgle Ads account. The impressions are broken down per campaigns per geo and do not include the display ads'),

                                
                          ]
                          ),
                          
                html.Div(className=' eight columns div-for-charts bg-grey',
                          children=[
                    
                                dcc.Graph(id='sem_ads', config={'displayModeBar': False}), #Ad Covnversion Rate Graph
                                html.Br(), 
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

                                dcc.Graph(id='sem_ctr', config={'displayModeBar': False}), #Ad Click-Through Rate Graph
                                html.Br(), 
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

                                dcc.Graph(id='sem_imp', config={'displayModeBar': False}), #Ad Impressions Graph
                                html.Br(), 
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
                  colorway=["#359EC3", '#D59353', '#B15AE6', '#6BBF5D', '#D45950'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Google Ad Campaigns Conversion Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_sem_nine.index.min(), df_sub_sem_nine.index.max()]},
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
                  colorway=["#359EC3", '#D59353', '#B15AE6', '#6BBF5D', '#D45950'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Google Ad Campaigns Click-Through Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_sem_ten.index.min(), df_sub_sem_ten.index.max()]},
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
                  colorway=["#359EC3", '#D59353', '#B15AE6', '#6BBF5D', '#D45950'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Google Ad Campaigns Impressions', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_sem_el.index.min(), df_sub_sem_el.index.max()]},
              ),

              }

    return figure

