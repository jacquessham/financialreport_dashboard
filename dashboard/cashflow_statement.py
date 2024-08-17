import pandas as pd
import cashflow_googl_poc as example
from data.googl.cashflow_googl import *


# Function called by dashboard.py
def cashflow_statement_figure(company, data):
	if company == 'googl':
		return cashflow_statement_GOOGL(data)
	return None
