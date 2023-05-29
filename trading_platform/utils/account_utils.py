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

def get_available_balance(symbol):

    free = [i for i in client.get_account()['balances'] if i['asset'] == symbol][0]['free']

    return free
