from stocknews import StockNews

def get_news(ticker):
    news = StockNews(ticker)
    return news.get()

def get_news_sentiment(ticker):
    news = StockNews(ticker)
    return news.get_sentiment()

def main(symbol):
    ticker = symbol
    news = get_news(ticker)
    sentiment = get_news_sentiment(ticker)

    print("Latest News:")
    for i in range(5):
        print(f"{i+1}. {news[i]['title']}")
        print(f"   Sentiment: {sentiment[i]['sentiment']}")
        print()

if __name__ == "__main__":
    main()
