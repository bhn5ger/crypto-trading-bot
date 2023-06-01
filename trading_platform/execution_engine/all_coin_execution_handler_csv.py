import os 
from binance.client import Client
import websocket, json
import pandas as pd
import datetime as dt
import sys
sys.path.insert(1, '../utils')
import all_coin_utils, account_utils

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

SPOT_TRADING_API_KEY = os.environ.get('spot_trading_binance_api')
SPOT_TRADING_API_SECRET = os.environ.get('spot_trading_binance_secret')

client = Client(API_KEY, API_SECRET) # Might have to use spot trading
symbols = os.listdir('/home/briann.briannn/crypto-trading-bot/trading_platform/data_stream/csvs') # Use relative path before deploying to production

