import os
import sqlalchemy
import pandas as pd
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET)

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')

def get_cumulative_returns(lookback):

    df = pd.read_sql('BTCUSDT', engine)
    lookbackperiod = df.iloc[-lookback:]
    cumret = (lookbackperiod.Price.pct_change() + 1).cumprod() - 1

    return cumret

