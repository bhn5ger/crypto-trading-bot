import os
import pandas as pd
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

print(API_KEY, API_SECRET)

client = Client(API_KEY, API_SECRET, tld='us')

#First get BTC price
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

# Calculate how much BTC $97 can buy
buy_quantity = 97 / float(btc_price['price'])

print(float(btc_price['price']) * buy_quantity)

print(buy_quantity)

'''
info = client.get_account()

df = pd.DataFrame(info["balances"])
df["free"] = df["free"].astype(float).round(4)
df = df[df["free"] > 0]
print(df)
'''

# Create test order
order = client.create_test_order(
        symbol='BTCUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=buy_quantity
    )



