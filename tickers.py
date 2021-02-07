import pandas as pd

def get_all_tickers(filename):
    data = pd.read_csv(filename)
    tickers = data.iloc[:,0]
    return list(tickers)
