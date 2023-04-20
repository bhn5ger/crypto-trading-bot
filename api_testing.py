import os
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

print(API_KEY, API_SECRET)

client = Client(API_KEY, API_SECRET, tld='us')

#First get USDT price
usdt_price = client.get_symbol_ticker(symbol="USDT")

# Calculate how much USDT $200 can buy
buy_quantity = round(200 / float(usdt_price['price']))

print(usdt_price['price'])

'''
# Create test order
order = client.create_test_order(
        symbol='BTCUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=buy_quantity
    )
'''


