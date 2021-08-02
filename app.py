# Importing Required Modules for the App
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
import flask


external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Tangerine&display=swap',
    {
        'href': 'https://fonts.googleapis.com/css2?family=Tangerine&display=swap',
        'rel': 'stylesheet',
        'crossorigin': 'anonymous'
    },

    'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Mono:ital,wght@1,100&display=swap',

    {
        'href': 'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Mono:ital,wght@1,100&display=swap',
        'rel': 'stylesheet',
        'crossoriging': 'anonymous'
    },

    'static/bootstrap.min.css',
    {
        'href': 'static/bootstrap.min.css',
        'rel': 'stylesheet',
        'crossorigin': 'anonymous'
    },

]



# Initializing the App
app = dash.Dash(__name__,  external_stylesheets=external_stylesheets, title='Python Data Visualization - Plotly & Dash Dashboard', suppress_callback_exceptions=True)

server = app.server


