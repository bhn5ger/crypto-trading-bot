import os
import pandas as pd
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(tld='us')


while True:

    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    
    print("       ", float(btc_price['price']))

