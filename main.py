from tickers import *
from fetch import *

all_tickers = get_all_tickers("bats_symbols.csv")

for ticker in all_tickers:
    print(get52WeekPriceChange(ticker))
