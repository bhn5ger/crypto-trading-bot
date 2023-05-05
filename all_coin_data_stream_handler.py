import os 
import pandas as pd
import sqlalchemy
import asyncio
from binance.client import Client 
from binance import AsyncClient, BinanceSocketManager

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

engine = sqlalchemy.create_engine('sqlite:///CryptoDB.db')

client = Client()

info = client.get_exchange_info()

symbols = [x['symbol'] for x in info['symbols']]
exclude = ['UP', 'DOWN', 'BEAR', 'BULL']
non_lev = [symbol for symbol in symbols if all(excludes not in symbol for excludes in exclude)]
relevant = [symbol for symbol in non_lev if symbol.endswith('USDT')]
multi = [i.lower() + '@trade' for i in relevant]



