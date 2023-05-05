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

engine = sqlalchemy.create_engine('sqlite:///CryptoDB.db')

symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type="table"', engine).name.to_list()

print(symbols)

