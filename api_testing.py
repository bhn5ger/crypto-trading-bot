import asyncio
import os
import pandas as pd
from binance.client import Client 
from binance import AsyncClient, BinanceSocketManager


API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

SPOT_TRADING_API_KEY = os.environ.get('spot_trading_binance_api')
SPOT_TRADING_API_SECRET = os.environ.get('spot_trading_binance_secret')

client = Client(API_KEY, API_SECRET)
spot_trading_client = Client(SPOT_TRADING_API_KEY, SPOT_TRADING_API_SECRET, tld='us')

'''
BUY RESPONSE

{'symbol': 'BTCUSDT', 'orderId': 1005200732, 'orderListId': -1, 'clientOrderId': 'HHk7NO6aPVikgxYnrzKlfN', 
'transactTime': 1683392507234, 'price': '0.00000000', 'origQty': '0.00300000', 'executedQty': '0.00300000',
'cummulativeQuoteQty': '86.05938000', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 
'side': 'BUY', 'workingTime': 1683392507234, 'fills': [{'price': '28686.46000000', 'qty': '0.00300000', 
'commission': '0.00000000', 'commissionAsset': 'BNB', 'tradeId': 23006532}], 'selfTradePreventionMode': 
'EXPIRE_MAKER'}

'''

order = spot_trading_client.create_order(
                            symbol='BTCUSDT',
                            side=Client.SIDE_BUY,
                            type=Client.ORDER_TYPE_MARKET,
                            quantity=0.0001                                      
                        )

print(order)
