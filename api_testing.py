import os
import pandas as pd
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us')

'''
BUY RESPONSE

{'symbol': 'BTCUSDT', 'orderId': 988476733, 'orderListId': -1, 'clientOrderId': '5GbaUurWYkpCEHTSjPvoxN', 
'transactTime': 1681984758356, 'price': '0.00000000', 'origQty': '0.00010000', 'executedQty': '0.00010000', 
'cummulativeQuoteQty': '2.88652000', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 
'side': 'BUY', 'workingTime': 1681984758356, 'fills': [{'price': '28865.20000000', 'qty': '0.00010000', 
'commission': '0.00000000', 'commissionAsset': 'BNB', 'tradeId': 22187132}], 'selfTradePreventionMode': 
'EXPIRE_MAKER'}
'''

while True:

    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    
    print(float(btc_price['price']))

    if float(btc_price['price']) > 29000:

        order = client.create_order(
                                    symbol='BTCUSDT',
                                    side=Client.SIDE_SELL,
                                    type=Client.ORDER_TYPE_MARKET,
                                    quantity=0.0001                                                
                                )

        print("order")

        break

