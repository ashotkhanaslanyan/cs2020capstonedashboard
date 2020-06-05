import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from common.server import app

class PlayersTab:

	def __init__(self):
		pass

	def getTab():
		return html.Div(children=[
			html.H2('HistogramTab',
				style={
					'margin': '5px'
				})
			])