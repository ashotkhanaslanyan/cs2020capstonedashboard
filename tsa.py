import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

from server import app
from tsa_dropdowns import *

transfers = pd.read_pickle("./data/eda/transfers_eda_data.pkl").dropna(subset=["fee","mv","age","year"]).sort_values(by = "year")
markval = pd.read_pickle("./data/eda/markval_eda_data.pkl").dropna(subset=["mv","age","cum_mv","last_year_mv","year"]).sort_values(by = "year")
transfers = transfers[transfers.age >= 16]
markval = markval[markval.age >= 16]

tsa_df = transfers

dropdowns = [
    html.P(["df" + ":", dcc.Dropdown(id = "ts_df", options = df_options, value = "transfers")]),
    html.P(["x" + ":", dcc.Dropdown(id = "ts_x", options = x_options, value = "year")]),
    html.P(["y" + ":", dcc.Dropdown(id = "ts_y", options = y_options, value = "fee")]),
    html.P(["color" + ":", dcc.Dropdown(id = "ts_color", options = cat_options)]),
    html.P(["facet_col" + ":", dcc.Dropdown(id = "ts_facet_col", options = cat_options)]),
    html.P(["facet_row" + ":", dcc.Dropdown(id = "ts_facet_row", options = cat_options)]),
    html.P(["summarizer" + ":", dcc.Dropdown(id = "summarizer", options = summarizers, value = "mean")])
]

tsa_tab = dcc.Tab(
    label = "Time Series Analysis",
    value = "tsa_tab",
    children = [
        html.Div(
            dropdowns,
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="tsa_graph", style={"width": "75%", "display": "inline-block"})
    ]
)

tsa_inputs = [
    Input("ts_x", "value"),
    Input("ts_y", "value"),
    Input("ts_color", "value"),
    Input("ts_facet_col", "value"),
    Input("ts_facet_row", "value"),
    Input("summarizer", "value")
]

@app.callback([
    Output("ts_y","value"),
    Output("ts_color","value"),
    Output("ts_x","options"),
    Output("ts_y","options"),
    Output("ts_color","options"),
    Output("ts_facet_col","options"),
    Output("ts_facet_row","options"),
    Output("summarizer","options"),
    ],
    [Input("ts_df", "value")])
def update_selectors(df):
    if(df == "markval"):
        global tsa_df
        tsa_df = markval
        return ("mv","league_class",x_options,mv_y_options,mv_cat_options,mv_cat_options,mv_cat_options,summarizers)
    else:
        tsa_df = transfers
        return ("fee","type",x_options,y_options,cat_options,cat_options,cat_options,summarizers)



@app.callback(Output("tsa_graph", "figure"), tsa_inputs)
def tsa_figrue(x,y,color,facet_col,facet_row,summarizer='mean'):
    agg_cols = []
    groups = [x,color,facet_col,facet_row]
    for var in groups:
        if((var is not None) and (var in tsa_df.columns)):
            agg_cols.append(var)
    graph_df = tsa_df.copy()
    df = graph_df.groupby(agg_cols).agg({y:summarizer}).reset_index()
    fig = px.line(
        df,
        x,
        y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        facet_col_wrap=4
    )
    if(not(facet_col is None) or not(facet_row is None)):
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))

    return fig