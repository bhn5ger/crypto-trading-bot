import os
import market_data_utils
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us')

# lookback is in seconds

def strategy(entry, lookback, qty, open_position=False):

    if not open_position:

        while True:

            look_back_period = market_data_utils.get_lookback_period(lookback)
            cum_ret = market_data_utils.get_cumulative_returns(look_back_period)

            print(cum_ret[cum_ret.last_valid_index()])
            print(entry)
            print('---------------------------------')

            if cum_ret[cum_ret.last_valid_index()] > entry:

                order = client.create_order(
                                            symbol='BTCUSDT',
                                            side='BUY',
                                            type='MARKET',
                                            quantity=qty
                                           )
                
                print(order)
                open_position = True
                break

    
    if open_position:
        
        while True:
            
            since_buy = market_data_utils.get_price_data_since_buy(order['transactTime'])

            if len(since_buy) > 1:

                since_buy_ret = market_data_utils.get_cumulative_returns(since_buy)
                last_entry = since_buy_ret[since_buy_ret.last_valid_index()]

                if last_entry > 0.0015 or last_entry < -0.0015:

                    order = client.create_order(
                                                symbol='BTCUSDT',
                                                side='SELL',
                                                type='MARKET',
                                                quantity=qty                                                
                                               )
                    
                    print(order)
                    break
    
strategy(0.0001, 60, 0.001)



    