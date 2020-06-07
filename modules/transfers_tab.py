import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import math
from dfply import *
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statistics 
import plotly.graph_objects as go
from scipy import stats
from scipy.stats import pearsonr
import plotly.graph_objects as go
import warnings
from scipy.stats import shapiro
from datetime import date, timedelta

from common.server import app
from common.dataframes import DataTables
from common.helpers.tfee_eda_helpers import *

transfers_eda = DataTables.transfers_eda

plot_types = {'scatter plot': 'scatter', 'line chart': 'line'}

plot_options = {
	'scatter': {
		'axis': {'Player\'s age': 'age', 'Market value': 'mv', 'Year of transfer': 'year'},
		'facet': {'none': 'none', 'continent': 'continent', 'position': 'main_field_position', 'both': 'both'}
	},
	'line': {
		'axis': {'Player\'s age': 'age', 'Year of transfer': 'year'},
		'facet': {'none': 'none', 'position': 'main_field_position', 'transfer type': 'type'}
	}
}

class TransfersTab:

	def __init__(self):
		pass

	def getTab():
		return html.Div(children = [
			html.Div(children=[
				html.H6('Plot type: ',
					style={
						'margin-left': '10px'
					}
				),
				dcc.Dropdown(
					id='tt_plot_selector',
					options=[{'label': i, 'value': plot_types[i]} for i in plot_types],
					value='scatter',
					style={
						'width': '95%',
						'margin-bottom': '2px',
						'margin-left': '5px',
						'float': 'left'
					}
				),
				html.H6('X axis: ',
					style={
						'margin-top': '3px',
						'margin-left': '10px'
					}
				),
				dcc.Dropdown(
					id='tt_x_axis_value',


					style={
						'width': '95%',
						'margin-bottom': '2px',
						'margin-left': '5px',
						'float': 'left'
					}
				),
				html.H6('Facet: ',
					style={
						'margin-top': '3px',
						'margin-left': '10px'
					}
				),
				dcc.Dropdown(
					id='tt_facet_value',
					style={
						'width': '95%',
						'margin-bottom': '2px',
						'margin-left': '5px',
						'float': 'left'
					}
				),
				html.Div(children=[
					html.H6('Summarized by: ',
						style={
							'margin-left': '10px'
						}
					),
					dcc.Dropdown(
						id='tt_smrzd_selector',
						options=[{'label': i, 'value': i} for i in ['mean', 'median', 'range', 'min', 'max']],
						value='mean',
						style={
							'width': '95%',
							'margin-bottom': '2px',
							'margin-left': '5px',
							'float': 'left'
						}
					)],
					id='tt_smrzd_display',
					style={
						'display':'none'
					}
				)],
	            style={
	            	'margin-left': '5px',
	            	'width': '23%',
	            	'padding': '5px 5px 10px 5px',
	            	'background-color': '#c3d9de',
	            	'height': '100%',
	            	'border-radius': '20px',
	            	'float': 'left',
	            	'margin-top': '10px'
	            }
	        ),
	        dcc.Graph(
	        	id='tt_markval_plot', 
	        	style={
	        		'width': '75%', 
	        		'display': 'inline-block',
	        	}
	        )
        ])

@app.callback(
	[Output('tt_x_axis_value', 'options'),
	Output('tt_facet_value', 'options'),
	Output('tt_smrzd_display', 'style')],
	[Input('tt_plot_selector', 'value')])
def plotOptioins(plot):
	if(plot=='scatter'):
		smrzd_style = {'display': 'none'}
	else:
		smrzd_style = {'display': 'block'}
	return [{'label': i, 'value': plot_options[plot]['axis'][i]} for i in plot_options[plot]['axis']],\
		[{'label': i, 'value': plot_options[plot]['facet'][i]} for i in plot_options[plot]['facet']],\
		smrzd_style

@app.callback(
	[Output('tt_x_axis_value', 'value'),
	Output('tt_facet_value', 'value')],
	[Input('tt_x_axis_value', 'options'),
	Input('tt_facet_value', 'options')])
def setDropdownValues(axis_options, facet_options):
	return axis_options[0]['value'], facet_options[0]['value']

@app.callback(
	Output('tt_markval_plot', 'figure'),
	[Input('tt_plot_selector', 'value'),
	Input('tt_x_axis_value', 'value'),
	Input('tt_facet_value', 'value'),
	Input('tt_smrzd_selector', 'value')])
def plotGraph(plot, axis_val, facet_val, smrzd_val):
	if(plot=='scatter'):
		if(facet_val=='none'):
			return scatter(transfers_eda, axis_val, 'fee')
		elif(facet_val=='both'):
			return scatter(transfers_eda, axis_val, 'fee', facet_row=True)	
		else:
			return scatter(transfers_eda, axis_val, 'fee', facet=True, facet_var=facet_val)	
	else:
		if(facet_val=='none'):
			return transfers_by_time(transfers_eda, axis_val, summarizer=smrzd_val)
		else:
			return transfers_by_time(transfers_eda, axis_val, summarizer=smrzd_val, group_var=facet_val, facet=True)