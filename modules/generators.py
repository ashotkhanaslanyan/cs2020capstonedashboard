import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

class Generator:

	def __init__(self):
		pass

	def dashDataTable(dataframe):
	    return html.Div(
	        children=[dash_table.DataTable(
	            id='table',
	            columns=[{"name": i, "id": i} for i in dataframe.columns],
	            data=dataframe.to_dict('records')
	        )
	    ])
