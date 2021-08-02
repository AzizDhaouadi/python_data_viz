import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_auth
from app import app
from dashboards import google_analytics, google_ads, home

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
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
        return home.layout    
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)


