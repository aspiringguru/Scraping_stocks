'''
pip install pandas-datareader
https://pandas-datareader.readthedocs.io/en/latest/

'''

import pandas_datareader as pdr
df = pdr.get_data_fred('GS10')
#https://fred.stlouisfed.org/series/GS10
df.shape
df.head()

import pandas as pd
from pandas_datareader import data
# Set the start and end date
start_date = '1990-01-01'
end_date = '2019-04-27'
# Set the ticker
ticker = 'AMZN'
# Get the data
data = data.get_data_yahoo(ticker, start_date, end_date)
data.head()
data.shape

df = data.drop(['Volume'], axis=1)

import matplotlib.pyplot as plt
data['Adj Close'].plot()
df.plot()
plt.savefig('pandas_datareader_demo1.png')



import yfinance as yf
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
data.shape
data.head(10)

import yfinance as yf
stock_code = "GOLD.AX"
data = yf.download(stock_code, start="2017-01-01", end="2020-04-27")
data.shape
data.head(10)
df = yf.Ticker(stock_code)
df.info
df.actions
df.dividends



methods = [method_name for method_name in dir(msft) if callable(getattr(msft, method_name))]
for method in methods:
    print(method)

get_actions
get_balance_sheet
get_balancesheet
get_calendar
get_cashflow
get_dividends
get_earnings
get_financials
get_info
get_institutional_holders
get_isin
get_major_holders
get_recommendations
get_splits                                                                                                              get_sustainability                                                                                                      history                                                                                                                 option_chain

['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_download_options', '_get_fundamentals', '_options2df', 'get_actions', 'get_balance_sheet', 'get_balancesheet', 'get_calendar', 'get_cashflow', 'get_dividends', 'get_earnings', 'get_financials', 'get_info', 'get_institutional_holders', 'get_isin', 'get_major_holders', 'get_recommendations', 'get_splits', 'get_sustainability', 'history', 'option_chain']
#----------------------------------------------


import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")
hist

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
#empty dataframe
msft.quarterly_financials
#empty dataframe


# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance heet
msft.balance_sheet
#empty dataframe
msft.quarterly_balance_sheet
#empty dataframe

# show cashflow
msft.cashflow
#empty dataframe
msft.quarterly_cashflow
#empty dataframe

# show earnings
msft.earnings
#empty dataframe
msft.quarterly_earnings
#empty dataframe

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
opt = msft.option_chain('2020-05-01')
# data available via: opt.calls, opt.puts
opt.calls
opt.puts
list(opt.calls.columns)
['contractSymbol', 'lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'change', 'percentChange', 'volume', 'openInterest', 'impliedVolatility', 'inTheMoney', 'contractSize', 'currency']
