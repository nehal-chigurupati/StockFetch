from tickers import *
from fetch import *
from util import *


def get_all_52_week_price_changes():
    all_tickers = get_all_tickers("bats_symbols.csv")
    priceChanges = {}
    for ticker in all_tickers:
        priceChanges[ticker] = get52WeekPriceChange(ticker)
    return priceChanges

def find_lowest_returns(num):
    all_price_changes = get_all_52_week_price_changes()
    prices_only = list(all_price_changes.values())
    prices_only = clean_list(prices_only)
    sorted_prices = selection_sort(prices_only)
    greatest_decline_stocks = sorted_prices[0:num]

    return_stocks = {}

    for stock in all_price_changes:
        stock_price = all_price_changes[stock]
        if stock_price in greatest_decline_stocks:
            return_stocks[stock] = stock_price

    return return_stocks
