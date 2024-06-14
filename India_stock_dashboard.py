import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st
import plotly.express as px

st.title('Indian Stock Market Dashboard')

st.sidebar.title('Stock Selection')
selected_stock = st.sidebar.text_input('Enter Stock Symbol', 'RELIANCE')

st.sidebar.title('Moving Average Selection')
ma_days = st.sidebar.slider('Moving Average Days', 1, 50, 20)

st.write('Stock Selected:', selected_stock)
st.write('Moving Average Days:', ma_days)

# Fetch live data
stock_data = yf.Ticker(selected_stock + '.NS').history(period="1d")
stock_data['MA'] = stock_data['Close'].rolling(window=ma_days).mean()

fig = px.line(stock_data, x=stock_data.index, y=['Close', 'MA'], title='Stock Price with Moving Average')
st.plotly_chart(fig)
st.write('Stock Data')

st.write(stock_data)

st.write('Stock Data Statistics')

st.write(stock_data.describe())




