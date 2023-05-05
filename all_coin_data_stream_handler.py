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

print(client.get_exchange_info())



