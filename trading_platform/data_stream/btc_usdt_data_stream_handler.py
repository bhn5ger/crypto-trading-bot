import os 
import pandas as pd
import sqlalchemy
import asyncio
from binance.client import Client 
from binance import AsyncClient, BinanceSocketManager

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

def create_frame(msg):

    df = pd.DataFrame([msg])
    df = df.loc[:,['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit = 'ms')
    return df

async def main():

    client = Client(API_KEY, API_SECRET)
    bsm = BinanceSocketManager(client)
    socket = bsm.trade_socket('BTCUSDT')

    async with socket as ts:
        while True:
            msg = await ts.recv()
            frame = create_frame(msg)
            frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
            print(frame)

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')

loop = asyncio.get_event_loop()
msg = loop.run_until_complete(main())
