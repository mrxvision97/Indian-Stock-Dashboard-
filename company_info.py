import yfinance as yf

def get_company_info(symbol):
    stock = yf.Ticker(symbol + '.NS')
    info = stock.info

    company_info = {
        'Name': info.get('longName', 'N/A'),
        'About': info.get('longBusinessSummary', 'N/A')
    }
    return company_info

