import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np 

from resources.server import app
from resources.dataframes import DataTables

axis_values = ['one', 'two']

class ScatterTab:

	def __init__(self):
		pass

	def getTab():
		return html.Div(children=[
			html.Div(children=[
				html.H6('X axis',
					style={
						'margin-left': '10px',
						'float': 'left'
					}),
				dcc.Dropdown(
					id='x_axis_picker',
					options=[{'label': i, 'value': i} for i in axis_values],
					value='one',
					style={
						'width': '300px',
						'margin-top': '5px',
						'margin-bottom': '2px',
						'margin-left': '5px',
						'float': 'left'
					}
				)],
				style={
					'width': '48%',
					'float': 'left'
				}
			),
			html.Div(children=[
				html.H6('Y axis',
					style={
						'margin-left': '10px',
						'float': 'left'
					}),
				dcc.Dropdown(
					id='y_axis_picker',
					options=[{'label': i, 'value': i} for i in axis_values],
					value='two',
					style={
						'width': '300px',
						'margin-top': '5px',
						'margin-bottom': '2px',
						'margin-left': '5px',
						'float': 'left'
					}
				)],
				style={
					'width': '48%',
					'float': 'right'
				}
			),
			html.Div(children=[
				dcc.Graph(
					id='scat_plt'
				)],
				style={
					'padding': '0px',
					'display': 'inline-block',
					'white-space': 'nowrap',
					'height': '400px',
					'width': '98%'
				}
			),
			html.Div(children=[
				dcc.Slider(
			        id='sp_season_slider',
			        min=2006,
			        max=2019,
			        value=2019,
			        marks={str(year): str(year) for year in range(2006, 2020)},
			        step=1
			    )],
				style={
					'margin-top': '5px',
					'width': '99%',
					'display': 'inline-block',
					'white-space': 'nowrap'
				}
			)]
		)

# uncomment this

# @app.callback(
# 	Output('scat_plt', 'figure'),
# 	[Input('x_axis_picker', 'value'),
# 	Input('y_axis_picker', 'value'),
# 	Input('sp_season_slider', 'value')])

# add plot function

# def update_scat_plot(x, y, sson):
