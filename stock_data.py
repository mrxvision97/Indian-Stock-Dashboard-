# import yfinance as yf
# import pandas as pd
#
# def get_stock_data(symbol, ma_days):
#     stock_data = yf.Ticker(symbol + '.NS').history(period="1d", interval="1m")
#     stock_data['MA'] = stock_data['Close'].rolling(window=ma_days).mean()
#     return stock_data

import requests
import pandas as pd
import yfinance as yf

def get_all_stock_symbols():
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    response = requests.get(url)
    if response.status_code == 200:
        stocks = response.text.split("\n")[1:-1]  # Skip the header and last empty line
        stock_codes = [stock.split(",")[0] for stock in stocks]
        return stock_codes
    else:
        print(f"Error fetching stock codes. Status code: {response.status_code}")
        return []

def get_stock_data(symbol, ma_days, period):
    stock_data = yf.Ticker(symbol + '.NS').history(period=period)
    stock_data['MA'] = stock_data['Close'].rolling(window=ma_days).mean()
    return stock_data

