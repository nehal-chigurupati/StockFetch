from util import *
from week_52_period import *
from tickers import *
from fetch import *

all_tickers = get_all_tickers('nasdaq_non_etf.csv')

num_neg_intervals = {}

def get_all_num_intervals_negative():
    for ticker in all_tickers:
        num_neg_intervals[ticker] = get_num_intervals_negative(ticker, 52, 1)

    return num_neg_intervals

def get_downward_stocks(num):
    all_downward_stocks = get_all_num_intervals_negative()
    all_downward_num_intervals = clean_list(list(all_downward_stocks.values()))

    sorted_all_downward_num_intervals = selection_sort(all_downward_num_intervals)
    lenSortedIntervals = len(sorted_all_downward_num_intervals)
    selected_downward_num_intervals = sorted_all_downward_num_intervals[lenSortedIntervals - num:lenSortedIntervals]

    selected_tickers = {}
    for interval in selected_downward_num_intervals:
        selected_tickers[get_key(interval, all_downward_stocks)] = interval

    return selected_tickers

def get_all_sorted_downward_stocks():
    all_downward_stocks = get_all_num_intervals_negative()
    all_downward_num_intervals = clean_list(list(all_downward_stocks.values()))

    sorted_all_downward_num_intervals = selection_sort(all_downward_num_intervals)
    tickers = {}

    for interval in all_downward_num_intervals:
        tickers[get_key(interval, all_downward_stocks)] = interval
    return tickers
