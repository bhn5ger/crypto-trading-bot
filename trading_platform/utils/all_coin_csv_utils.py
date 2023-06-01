import asyncio
from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import datetime as dt
import os
import sqlalchemy
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us') 

symbols = os.listdir('/home/briann.briannn/crypto-trading-bot/trading_platform/data_stream/csvs') # Use relative path before deploying to production
