import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

#Importing options for selector inputs
#Importing the server app
from eda_dropdowns import *
from server import app
from tsa import tsa_tab
from data_tables import tables_tab

server = app.server

transfers = pd.read_pickle("./data/eda/transfers_eda_data.pkl").dropna(subset=["fee","mv","age"]).sort_values(by = "year")
markval = pd.read_pickle("./data/eda/markval_eda_data.pkl").dropna(subset=["mv","age","cum_mv","last_year_mv"]).sort_values(by = "year")

#options are imported from eda_dropdowns.py
dropdowns = [
    html.P(["df" + ":", dcc.Dropdown(id = "df", options = df_options, value = "transfers")]),
    html.P(["x" + ":", dcc.Dropdown(id = "x", options = numerical_options, value = "mv")]),
    html.P(["y" + ":", dcc.Dropdown(id = "y", options = numerical_options, value = "fee")]),
    html.P(["color" + ":", dcc.Dropdown(id = "color", options = categorical_options, value = "type")]),
    html.P(["facet_col" + ":", dcc.Dropdown(id = "facet_col", options = categorical_options)]),
    html.P(["facet_row" + ":", dcc.Dropdown(id = "facet_row", options = categorical_options)])
]

graph_df = transfers

app.layout = html.Div(
    children = [
        html.H1("Soccer Market Analysis"),
        dcc.Tabs(
            id='all_tabs',
            value='datasets',
            children = [
                tables_tab,
                dcc.Tab(
                label = "Exploratory Analysis",
                value = "transfers_tab",
                children = [
                    html.Div(
                        dropdowns,
                        style={"width": "25%", "float": "left"},
                    ),
                    dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
                ]
                ),
                tsa_tab
            ]
        )
    ]
)


inputs = [
    Input("x", "value"),
    Input("y", "value"),
    Input("color", "value"),
    Input("facet_col", "value"),
    Input("facet_row", "value"),
]

hover_data = transfers_hover_data

@app.callback([
    Output("x","options"), 
    Output("y","options"),
    Output("color","options"),
    Output("facet_col","options"),
    Output("facet_row","options"),
    Output("x","value"), 
    Output("y","value"),
    ],
    [Input("df", "value")])
def change_selectors(df):
    if(df == "markval"):
        global graph_df
        global hover_data
        graph_df = markval
        hover_data = markval_hover_data
        values = (mv_numeric_options, mv_numeric_options, mv_categoric_options, 
        mv_categoric_options, mv_categoric_options, "cum_mv", "mv")
        return values
    else:
        graph_df = transfers
        hover_data = transfers_hover_data
        values = (numerical_options, numerical_options, categorical_options, 
        categorical_options, categorical_options, "mv", "fee")
        return values


@app.callback(Output("graph", "figure"), inputs)
def make_figure(x = None, y = None, color = None, facet_col = None, facet_row = None):
    fig = px.scatter(
        graph_df,
        x=x,
        y=y,
        color=color,
        hover_data=hover_data,
        facet_col=facet_col,
        facet_row=facet_row,
        trendline="ols",
        facet_col_wrap=4
    )
    if(not(facet_col is None) or not(facet_row is None)):
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))

    return fig


if __name__ == '__main__':
    app.run_server(debug=False)