import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_auth
import app
from app import app
from dashboards import google_analytics, google_ads, home


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard/google_analytics':
        return google_analytics.layout
    elif pathname == '/dashboard/google_ads':
        return google_ads.layout
    elif pathname == '/':
        return app.home()
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)


