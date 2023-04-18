import os 
import pandas as pd
import sqlalchemy
import asyncio
from binance.client import Client 
from binance import BinanceSocketManager

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

async def main():
    
    client = Client(API_KEY, API_SECRET)    
    bsm = BinanceSocketManager(client)
    socket = bsm.trade_socket('BTCUSDT')

    async with socket as ts:

        msg = await ts.recv()
        print(msg)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
