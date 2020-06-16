import plotly_express as px
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

from tsa import tsa_tab
from server import app

players = pd.read_pickle("./data/players_Clean.pkl")
# stats = pd.read_pickle("./data/stats_Clean.pkl")
transfers = pd.read_pickle("./data/transfers_Clean.pkl")
trophies = pd.read_pickle("./data/trophies_Clean.pkl")
markval = pd.read_pickle("./data/markval_Clean.pkl")

tables = [players, markval ,transfers, trophies]
table_names = ["Players", "Market Value", "Transfers", "Trophies"]


tables_tab = dcc.Tab(
    label = "Datasets",
    value = "datasets",
    children = [
        html.Div(children = [
            dcc.Dropdown(
                id = 'table_picker',
                options = [{'label': i, 'value': i} for i in table_names],
                value='Players',
            )
        ]),
        html.Div(children = [
            dash_table.DataTable(
                id = 'table',
                editable=True,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
            )
        ],
        style={
            'width': 'auto', 
            'flex': '1 1 auto',
            'margin': '5px',
            'overflow-y': 'auto',
            'border-bottom': '1px solid #b8b8b8', 
            'border-left': '1px solid #b8b8b8',
            'border-top': '1px solid #b8b8b8'
        },         
        )
    ]
)

@app.callback(
    [
        Output('table','columns'),
        Output('table','data')
    ],
    [
        Input('table_picker','value')
    ]
)
def update_table(table_name):
	global tables
	table_index = table_names.index(table_name)
	return \
        [{"name": i, "id": i} for i in tables[table_index].columns],\
        tables[table_index].to_dict('records')
