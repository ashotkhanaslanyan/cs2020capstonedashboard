import dash

app = dash.Dash(
    __name__, 
    external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])

app.config['suppress_callback_exceptions']=True