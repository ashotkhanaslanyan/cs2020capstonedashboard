import dash
import dash_core_components as dcc
import dash_html_components as html

from resources.server import app
from modules.tables_tab import TableTab
from modules.scatter_tab import ScatterTab
from modules.boxplot_tab import BoxPlotTab
from modules.histogram_tab import HistoTab
from modules.linechart_tab import LineChartTab
from modules.heatmap_tab import HeatMapTab

server = app.server

app.layout = html.Div(children=[
	dcc.Tabs(
		id="tabs-with-classes",
		value='scat_tab',
		parent_className='custom-tabs',
		className='custom-tabs-container',
		children=[
			dcc.Tab(
		        label='Tables',
		        value='tbl_tab',
		        children=[
		        	TableTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Scatterplots',
		        value='scat_tab',
		        children=[
		        	ScatterTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Boxplots',
		        value='bplot_tab',
		        children=[
		        	BoxPlotTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Histograms',
		        value='hist_tab', 
		        children=[
		        	HistoTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Line Charts',
		        value='line_tab',
		        children=[
		        	LineChartTab.getTab()
		        ]
		    ),
		    dcc.Tab(
		        label='Heatmaps',
		        value='hmap_tab',
		        children=[
		        	HeatMapTab.getTab()
		        ]
		    )
		],
		style={
			'margin': '0px'
			}
		),

	html.Div(id='tabs-content-classes')],
	style={'margin': '-8px'}
)

if(__name__=='__main__'):
   app.run_server(debug=True)
