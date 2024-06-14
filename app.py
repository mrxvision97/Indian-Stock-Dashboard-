import streamlit as st
import plotly.express as px
import stock_data
import company_info
import financial_ratios
import financial_news


st.title('Indian Stock Market Dashboard')

# Get a list of all available stock symbols
all_stocks = stock_data.get_all_stock_symbols()

st.sidebar.title('Stock Selection')
selected_stock = st.sidebar.selectbox('Select Stock', all_stocks)

# Fetch company information for the selected stock
company_info_data = company_info.get_company_info(selected_stock)

# Print the stock symbol and company name on the home page
st.write(f'Stock Selected: {selected_stock} - {company_info_data["Name"]}')

# Fetch company information
st.subheader('About the Company')
st.write(company_info_data['Name'])
st.write(company_info_data['About'])

st.sidebar.title('Moving Average Selection')
ma_days = st.sidebar.slider('Moving Average Days', 1, 50, 20)

# Time period selection below the graph
st.subheader('Select Time Period for Analysis')
period = st.selectbox('Select Time Period', ['1d', '5d', '1mo', '3mo', '6mo', '1y'])

# Fetch live data based on the selected period
try:
    stock_df = stock_data.get_stock_data(selected_stock, ma_days, period)
    fig = px.line(stock_df, x=stock_df.index, y='Close', title='Stock Price')
    fig.add_scatter(x=stock_df.index, y=stock_df['MA'], mode='lines', name='Moving Average')
    st.plotly_chart(fig)
    st.write('Stock Data')
    st.write(stock_df)

    st.write('Stock Data Statistics')
    st.write(stock_df.describe())
except Exception as e:
    st.write(f'Error fetching stock data: {e}')

st.write('Moving Average Days:', ma_days)



