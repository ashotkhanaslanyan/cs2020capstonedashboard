import pandas as pd
import numpy as np

class DataTables:

	players = pd.read_pickle('data/players_Clean.pkl')
	market_value = pd.read_pickle('data/markval_Clean.pkl')
	national_stats_full = pd.read_pickle('data/natstats_Clean.pkl')
	national_stats = national_stats_full[0:100000]
	stats_full = pd.read_pickle('data/stats_Clean.pkl')
	stats = stats_full[0:100000]
	transfers = pd.read_pickle('data/transfers_Clean.pkl')
	trophies = pd.read_pickle('data/trophies_Clean.pkl')
	markval_prev_eda = pd.read_pickle('data/eda/markval_prev_eda.pkl')
