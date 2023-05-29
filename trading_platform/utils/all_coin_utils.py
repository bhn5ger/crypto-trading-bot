import asyncio
from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import datetime as dt
import os
import sqlalchemy
from binance.client import Client # not necessary?

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us') # not necessary?

current_directory = os.getcwd()
relative_path = '../data_stream/CryptoDB.db'
absolute_path = os.path.abspath(os.path.join(current_directory, relative_path))

engine = sqlalchemy.create_engine('sqlite:///' + absolute_path)

symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type="table"', engine).name.to_list()

def get_coin_price_in_past_n_minutes(symbol, lookback):

    now = dt.datetime.now() + dt.timedelta(hours=4) # Convert EST to Binance time which is in UTC
    before = now - dt.timedelta(minutes=lookback)
    qry_str = f"""SELECT * FROM '{symbol}' WHERE TIME >= '{before}'"""
    return pd.read_sql(qry_str, engine)

def get_coin_with_greatest_cumulative_returns_in_past_n_minutes(lookback):
    
    returns = [] # 0.015 -> 1.5% cumulative return
    for symbol in symbols:
        prices = get_coin_price_in_past_n_minutes(symbol, lookback).Price
        cumret = (prices.pct_change() + 1).prod() - 1
        returns.append(cumret)

    top_coin = symbols[returns.index(max(returns))]
    
    return top_coin 

def get_minimum_permitted_investment_qty(symbol):

    info = client.get_symbol_info(symbol=symbol)
    lotsize = float([i for i in info['filters'] if i['filterType'] == 'LOT_SIZE'][0]['minQty'])

    return lotsize
