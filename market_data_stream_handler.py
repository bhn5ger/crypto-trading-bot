import os 
import pandas as pd
import sqlalchemy
from binance.client import Client 
from binance import BinanceSocketManager

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
bsm = BinanceSocketManager(client)
socket = bsm.trade_socket('BTCUSDT')

async def get_data():
    await socket.__aenter__()
    msg = await socket.recv()
    print(msg)

