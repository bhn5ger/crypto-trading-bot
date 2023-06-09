import os
import sqlalchemy
import pandas as pd
from binance.client import Client # not necessary?

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us') # not necessary?

current_directory = os.getcwd()
relative_path = '../data_stream/BTCUSDTstream.db'
absolute_path = os.path.abspath(os.path.join(current_directory, relative_path))

engine = sqlalchemy.create_engine('sqlite:///' + absolute_path)

def get_cumulative_returns(df):

    cumret = (df.Price.pct_change() + 1).cumprod() - 1

    return cumret

def get_lookback_period(lookback):

    df = pd.read_sql('BTCUSDT', engine)
    lookbackperiod = df.iloc[-lookback:]

    return lookbackperiod

def get_price_data_since_buy(txnt_time):

    df = pd.read_sql('BTCUSDT', engine)
    sincebuy = df.loc[df.Time > pd.to_datetime(txnt_time, unit='ms')]

    return sincebuy
