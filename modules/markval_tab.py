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
from IPython.display import Image
from dateutil.relativedelta import *
import datetime as dt

from common.server import app
from common.dataframes import DataTables
from common.helpers.mv_eda_helpers import *

players = DataTables.players
markval = DataTables.markval_prev_eda
markval = markval[markval.mv.notnull()]
markval = markval[markval.age.notnull()]
markval_out = markval[~markval.mv.between(markval.mv.quantile(.15), markval.mv.quantile(.85))]
top_leagues = ['LaLiga','Bundesliga','Serie A','Premier League',
          'Ligue 1','Liga NOS','Eredivisie','Liga MX Clausura',
          'MLS','Jupiler Pro League', 'Série A', 'Superliga']
markval_tt = markval[markval.league.isin(top_leagues)]

plot_types = {'scatter plot': 'scatter', 'line chart': 'line'}

plot_options = {
	'scatter': {
		'axis': {'Player\'s age': 'age', 'Previous year\'s market value': 'last_year_mv', 'Cumulative market value': 'cum_mv'},
		'facet': {'none': 'none', 'year': 'year', 'position': 'main_field_position'}
	},
	'line': {
		'axis': {'Player\'s age': 'age', 'Year': 'year'},
		'facet': {'none': 'none', 'position': 'main_field_position', 'top leagues': 'league', 'continent': 'continent'}
	}
}

class MarkValTab:

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
					id='mvt_plot_selector',
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
					id='mvt_x_axis_value',


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
					id='mvt_facet_value',
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
						id='mvt_smrzd_selector',
						options=[{'label': i, 'value': i} for i in ['mean', 'median', 'range', 'min', 'max']],
						value='mean',
						style={
							'width': '95%',
							'margin-bottom': '2px',
							'margin-left': '5px',
							'float': 'left'
						}
					)],
					id='mvt_smrzd_display',
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
	        	id='mvt_markval_plot', 
	        	style={
	        		'width': '75%', 
	        		'display': 'inline-block',
	        	}
	        )
        ])

@app.callback(
	[Output('mvt_x_axis_value', 'options'),
	Output('mvt_facet_value', 'options'),
	Output('mvt_smrzd_display', 'style')],
	[Input('mvt_plot_selector', 'value')])
def plotOptioins(plot):
	if(plot=='scatter'):
		smrzd_style = {'display': 'none'}
	else:
		smrzd_style = {'display': 'block'}
	return [{'label': i, 'value': plot_options[plot]['axis'][i]} for i in plot_options[plot]['axis']],\
		[{'label': i, 'value': plot_options[plot]['facet'][i]} for i in plot_options[plot]['facet']],\
		smrzd_style

@app.callback(
	[Output('mvt_x_axis_value', 'value'),
	Output('mvt_facet_value', 'value')],
	[Input('mvt_x_axis_value', 'options'),
	Input('mvt_facet_value', 'options')])
def setDropdownValues(axis_options, facet_options):
	return axis_options[0]['value'], facet_options[0]['value']

@app.callback(
	Output('mvt_markval_plot', 'figure'),
	[Input('mvt_plot_selector', 'value'),
	Input('mvt_x_axis_value', 'value'),
	Input('mvt_facet_value', 'value'),
	Input('mvt_smrzd_selector', 'value')])
def plotGraph(plot, axis_val, facet_val, smrzd_val):
	if(plot=='scatter'):
		return scatter_mv_change(markval, axis_val, markval.mv, facet_val)
	else:
		if(facet_val=='league'):
			return markval_by_time(markval_tt, axis_val, smrzd_val, facet_val, legend=False, group_var='league')
		elif(facet_val=='continent'):
			return markval_by_time(markval, axis_val, smrzd_val, facet_val, group_var='continent')
		else:
			return markval_by_time(markval, axis_val, smrzd_val, facet_val)	

