import yfinance as yf
import pandas as pd
import datetime
from tickers import get_all_tickers
from util import *

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

def get_price_history(ticker, numWeeks, interval):
    tickerData = yf.Ticker(ticker)

    today = datetime.date.today()
    start_date = today - datetime.timedelta(weeks=numWeeks)

    if (is_weekday(today) == True and is_weekday(start_date) == True):
        tickerData = yf.Ticker(ticker)
        stringed_start_date = get_properly_formatted_date(start_date)
        stringed_end_date = get_properly_formatted_date(today)
        priceHistory = tickerData.history(period='1d', start=stringed_start_date, end=stringed_end_date)
    else:
        if get_day_of_week(today) == "Saturday":
            end_date = today - datetime.timedelta(days=1)
        elif get_day_of_week(today) == "Sunday":
            end_date = today - datetime.timedelta(days=2)

        if get_day_of_week(start_date) == "Saturday":
            start_date = start_date - datetime.timedelta(days=1)
        elif get_day_of_week(start_date) == "Sunday":
            start_date = start_date - datetime.timedelta(days=2)
        stringed_start_date = get_properly_formatted_date(start_date)
        stringed_end_date = get_properly_formatted_date(end_date)

        period = str(interval) + "w"

        priceHistory = tickerData.history(period=period, start=stringed_start_date, end=stringed_end_date)

    return priceHistory

def get_price_change(ticker, numWeeks):
    try:
        priceHistory = get_price_history(ticker, numWeeks)
        oldPrice = data.head(1).iat[0, 0]
        newPrice = data.tail(1).iat[0, 0]

        changeInPrice = (newPrice - oldPrice) / (oldPrice)

        return changeInPrice
    except:
        print("error")
        return 'NULL'

def get_num_intervals_negative(ticker, numWeeks, interval):
    priceHistory = get_price_history(ticker, numWeeks, interval)
    prices = list(priceHistory["Open"])
    numNegativeIntervals = 0

    for index in range(0, len(prices) - 1):
        price_change = (prices[index+1] - prices[index]) / (prices[index])
        if price_change < 0:
            numNegativeIntervals = numNegativeIntervals + 1

    return numNegativeIntervals
