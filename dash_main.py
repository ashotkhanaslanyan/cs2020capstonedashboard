import dash
import dash_core_components as dcc
import dash_html_components as html

from common.server import app
from modules.tables_tab import TableTab
from modules.markval_tab import MarkValTab
from modules.transfers_tab import TransfersTab

server = app.server

app.title = 'Sport Stat'
app.layout = html.Div(children=[
	dcc.Tabs(
		id="tabs-with-classes",
		value='mv_tab',
		parent_className='custom-tabs',
		className='custom-tabs-container',
		children=[
			dcc.Tab(
		        label='Data Tables',
		        value='tbl_tab',
		        children=[
		        	TableTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Market Values',
		        value='mv_tab',
		        children=[
		        	MarkValTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Transfers Fee',
		        value='tf_tab',
		        children=[
		        	TransfersTab.getTab()
		        ]
		    )
		],
		style={
			'margin': '0px',
			'flex': '0 1 auto'
			}
		),

		html.Div(id='tabs-content-classes')
	],
	style={
		'margin': '-8px',
		  'display': 'flex',
		  'flex-flow': 'column',
		  'height': '98vh'
    }
)

if(__name__=='__main__'):
   app.run_server(debug=True)
