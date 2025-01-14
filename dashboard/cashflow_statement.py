import pandas as pd
import data.googl.poc_charts.cashflow_googl_poc as example  # For poc purpose, delete later
from data.googl.cashflow_googl import *
from data.aapl.cashflow_aapl import *
from data.meta.cashflow_meta import *
from data.bac.cashflow_bac import *
from data.ge.cashflow_ge import *
from data.nvda.cashflow_nvda import *


# Function called by dashboard.py
def cashflow_statement_figure(company, data):
	if company == 'googl':
		return cashflow_statement_GOOGL(data)
	elif company == 'aapl':
		return cashflow_statement_AAPL(data)
	elif company == 'meta':
		return cashflow_statement_META(data)
	elif company == 'bac':
		return cashflow_statement_BAC(data)
	elif company == 'ge':
		return cashflow_statement_GE(data)
	elif company == 'nvda':
		return cashflow_statement_NVDA(data)
	return None
