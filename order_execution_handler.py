import os
import market_data_utils
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET)

def strategy(entry, lookback, qty, open_position=False):

    while True:
        
        cum_ret = market_data_utils.get_cumulative_returns(lookback)

        if not open_position:

            if cum_ret[cum_ret.last_valid_index()] > entry:

                order = client.create_order(symbol='BTCUSDT',
                                            side='BUY',
                                            type='MARKET',
                                            quantity=qty
                                           )
                
                print(order)
                open_position = True
                break

    
    if open_position:
        
        while True:
            pass

    