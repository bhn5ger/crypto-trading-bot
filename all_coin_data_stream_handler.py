import os 
import pandas as pd
import sqlalchemy
import asyncio
from binance.client import Client 
from binance import AsyncClient, BinanceSocketManager

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

engine = sqlalchemy.create_engine('sqlite:///CryptoDB.db')

client = Client()

info = client.get_exchange_info()

symbols = [x['symbol'] for x in info['symbols']]
exclude = ['UP', 'DOWN', 'BEAR', 'BULL']
non_lev = [symbol for symbol in symbols if all(excludes not in symbol for excludes in exclude)]
relevant = [symbol for symbol in non_lev if symbol.endswith('USDT')]
multi = [i.lower() + '@trade' for i in relevant]

def create_frame(msg):

    df = pd.DataFrame([msg['data']])
    df = df.loc[:,['s','E','p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df

async def main():

    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ms = bm.multiplex_socket(multi)

    async with ms as tscm:
        while True:
            msg = await tscm.recv()
            if msg:
                frame = create_frame(msg)
                frame.to_sql(frame.symbol[0], engine, if_exists='append', index=False)
                print(pd.read_sql('BTCUSDT', engine))
                
    await client.close_connection()


loop = asyncio.get_event_loop()
msg = loop.run_until_complete(main())

 



