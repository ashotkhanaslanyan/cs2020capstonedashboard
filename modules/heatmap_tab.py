import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from resources.server import app

class HeatMapTab:

	def __init__(self):
		pass

	def getTab():
		return html.Div(children=[
			html.H2('HeatMapTab',
				style={
					'margin': '5px'
				})
			])