import yfinance as yf
import pandas as pd
from tickers import get_all_tickers

def get52WeekPriceHistory(ticker):
    tickerData = yf.Ticker(ticker)
    priceHistory = tickerData.history(period='1d', start='2020-2-7', end='2021-2-5')

    return priceHistory

def get52WeekPriceChange(ticker):
    try:
        data = get52WeekPriceHistory(ticker)
        oldPrice = data.head(1).iat[0, 0]
        newPrice = data.tail(1).iat[0, 0]

        changeInPrice = (newPrice - oldPrice) / (oldPrice)

        return changeInPrice
    except:
        return 'NULL'
