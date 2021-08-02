
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
            html.A('Primary Reports', href='/apps/app1', style={'color': '#FFF'}, target='_blank', className='menu-nav')
        ]
        ),
        html.Li(style={'display': 'inline-block', 'margin-left': '40px'}, children=[
            html.A('SEM Reports', href='/apps/app2', style={'color': '#FFF'}, target='_blank', className='menu-nav')
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
                              html.H1('TOUR PAGES', style={'margin-top': '-6em'}),

                              #Drowdown Menu for the pageviews
                              html.H2('Pageviews', style={'color': '#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '2em'}),  
                              html.P('What is being visualized are not unique pageviews. Unique pageviews are not supportted yet!'),
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='stockselector',
                                                        options=get_options(df['Page'].unique()),
                                                          multi=True,
                                                        value=[df['Page'].sort_values()[0]],
                                                        style={'backgroundColor': '#1E1E1E'},
                                                        className='stockselector')
                                       ],
                                       style={'color': '#1E1E1E'}),
                                html.P('Graph last updated on 01/04/2021', style={'fontSize': 'smaller', 'color': '#DBDBDB'}),

                                #Dropdown for the Bounce rate
                                html.H2('Bounce Rate', style={'color': '#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='bounceselector',
                                                          options=get_options(df_two['Bounce'].unique()),
                                                          multi=True,
                                                          value=[df_two['Bounce'].sort_values()[0]],
                                                          style={'backgroundColor': '#1E1E1E'} ,
                                                          className='bounceselector')       
                                         ],
                                         style={'color': '#000'}),
                                html.P('Graph last updated on 01/04/2021', style={'fontSize': 'smaller', 'color': '#DBDBDB'}),

                                #Dropdown for the Exit rate
                                html.H2('Exit Rate', style={'color': '#299cb2', 'fontFamily': 'Playfair Display, serif', 'fontWeight': 'bolder', 'margin-top': '17em'}),
                                html.P('The exit rate referes to the number of customers leaving the site from said page after being active'),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='exitselector',
                                                          options=get_options(df_three['Exit'].unique()),
                                                          multi=True,
                                                          value=[df_three['Exit'].sort_values()[0]],
                                                          style={'backgroundColor': '#1E1E1E'} ,
                                                          className='exitselector')       
                                         ],
                                         style={'color': '#1E1E1E'}),
                                html.P('Graph last updated on 01/04/2021', style={'fontSize': 'smaller', 'color': '#DBDBDB'}),

                          ]
                          ),
                          
                html.Div(className=' eight columns div-for-charts bg-grey',
                          children=[
                              dcc.Graph(id='timeseries', config={'displayModeBar': False}), #Pageviews Graph
                              html.Br(), 

                              dcc.Graph(id='change', config={'displayModeBar': False}), # Bounce Rate Graph
                              html.Br(),

                              dcc.Graph(id='exit_rate', config={'displayModeBar': False}), # Exit Rate Graph
                              html.Br(), ])
             ]),

            html.Hr(style={'display': 'block', 'height': '1px',
                'border': '0', 'border-top': '1px solid #828282',
                'margin-top': '12em', 'padding': '0'}),
            
            html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                          children=[
                              html.H1('EVENTS', style={'margin-top': '-2em'}),
                                #Dropdown for the Events
                                html.H2('Events Tracking', style={'color': '#299cb2', 'fontFamily': 'Playfair Display, serif'}),
                                html.P('''Create campaign event refers to the action where the user creates the campaign and saves it without moving forward.
                                Campaign confirmation refers to the action of user finishing the set up of their campaigns and clicking the confirming campaign button'''),
                                html.Div(className='div-for-dropdown',
                                         children=[
                                             dcc.Dropdown(id='evenselector',
                                                          options=get_options(df_four['Event'].unique()),
                                                          multi=True,
                                                          value=[df_four['Event'].sort_values()[0]],
                                                          style={'backgroundColor': '#1E1E1E'} ,
                                                          className='evenselector')       
                                         ],
                                         style={'color': '#1E1E1E'}),
                                html.P('Graph last updated on 01/04/2021', style={'fontSize': 'smaller', 'color': '#DBDBDB'}),
                          ]
                          ),
                          
                html.Div(className=' eight columns div-user-controls bg-grey', style={'margin-top': '-5em'},
                          children=[
                              
                              dcc.Graph(id='event_tracking', config={'displayModeBar': False}), # Event Tracking Graph
        
                          ])
             ]),

            html.Hr(style={'display': 'block', 'height': '1px',
                'border': '0', 'border-top': '1px solid #828282', 'padding': '0'}),

             html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                          children=[
                              html.H1('HOW TO USE THE REPORTS', style={'margin-top': '-2em'}),
                                #Dropdown for the Events
                                html.P('''From the dropdown menu, select which pages or events you are interested in. You can select multiple page events
                                per graph for comparison.'''),
                          ]
                          ),
                          
                html.Div(className=' eight columns div-user-controls bg-grey', style={'margin-top': '-5em'},
                          children=[
                              html.H3('Graph Features'),

                              html.H6('Zooming on Graphs', style={'fontSize': 'smaller'}),
                              html.P('''You can zoom on graphs both horizontally and vertically. To default back to the intial state, double tap on the graph''',
                              style={'fontSize': 'smaller'}),
                              
                              html.H6('Moving Axes', style={'fontSize': 'smaller'}),
                              html.P('''To move along the x or y axis, drag the axis up or down''', style={'fontSize': 'smaller'}),

                              html.H6('Graph Legend', style={'fontSize': 'smaller'}),
                              html.P('''The graph legend shows which KPIs are being visualized. Click on the individual KPI to omit it from
                              the graph without using the dropdown menu.''', style={'fontSize': 'smaller'}),
                              
                              html.Br(),
                              html.Br(),
                              html.Br(),
                              html.Br()
                          ])
             ]),


])

# Update Pageviews
@app.callback(Output('timeseries', 'figure'),
                      [Input('stockselector', 'value')])
                      
def update_pageviews(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub = df
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['Page'] == stock].index,
                                y=df_sub[df_sub['Page'] == stock]['value'],
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
                #   title={'text': 'Pageviews', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure


# Update Bounce Rate
@app.callback(Output('change', 'figure'),
                      [Input('bounceselector', 'value')])
                      
def update_bouncerate(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_two = df_two
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_two[df_sub_two['Bounce'] == stock].index,
                                y=df_sub_two[df_sub_two['Bounce'] == stock]['value'],
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
                #   title={'text': 'Bounce Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_two.index.min(), df_sub_two.index.max()]},
              ),

              }

    return figure

# Update Exit Rate
@app.callback(Output('exit_rate', 'figure'),
                      [Input('exitselector', 'value')])
                      
def update_exitrate(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_three = df_three
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_three[df_sub_three['Exit'] == stock].index,
                                y=df_sub_three[df_sub_three['Exit'] == stock]['value'],
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
                #   title={'text': 'Exit Rate', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_three.index.min(), df_sub_three.index.max()]},
              ),

              }

    return figure

# Update Events Tracking
@app.callback(Output('event_tracking', 'figure'),
                      [Input('evenselector', 'value')])
                      
def update_eventstracking(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []
    df_sub_four = df_four
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub_four[df_sub_four['Event'] == stock].index,
                                y=df_sub_four[df_sub_four['Event'] == stock]['value'],
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
                #   title={'text': 'Event Tracking', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub_four.index.min(), df_sub_four.index.max()]},
              ),

              }

    return figure





