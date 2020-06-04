import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from resources.server import app
from resources.dataframes import DataTables

available_tables = ['Players', 'Market Value', 'National Stats', 'Stats', 'Transfers', 'Trophies']

class TableTab:

	def __init__(self):
		pass

	def getTab():
		global available_tables
		return html.Div(children=[
			dcc.Dropdown(
				id='table_picker',
				options=[{'label': i, 'value': i} for i in available_tables],
				value='Players',
				style={
					'width': '300px',
					'position': 'center',
					'margin-top': '5px',
					'margin-bottom': '5px',
					'margin-left': '2px'
				}
			),

			html.Div(
				children=[
					dash_table.DataTable(
						id='table'
					)
				],
				style={
					'width': 'auto', 
					'height': '500px',  
					'margin': '5px',
					'overflow-y': 'auto',
					'border-bottom': '1px solid #b8b8b8', 
					'border-left': '1px solid #b8b8b8',
					'border-top': '1px solid #b8b8b8'
					}, 
				)
			])

@app.callback(
	[Output('table', 'columns'),
	Output('table', 'data')],
	[Input('table_picker', 'value')]
)

def update_table(table_name):
	global available_tables
	table_index = available_tables.index(table_name)
	data_tables = [DataTables.players, DataTables.market_value, DataTables.national_stats, DataTables.stats, DataTables.transfers, DataTables.trophies]
	return \
        [{"name": i, "id": i} for i in data_tables[table_index].columns],\
        data_tables[table_index].to_dict('records')