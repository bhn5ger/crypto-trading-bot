import os
import sys
sys.path.insert(1, '../utils')
import btc_usdt_utils
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

SPOT_TRADING_API_KEY = os.environ.get('spot_trading_binance_api')
SPOT_TRADING_API_SECRET = os.environ.get('spot_trading_binance_secret')

client = Client(API_KEY, API_SECRET, tld='us')
spot_trading_client = Client(SPOT_TRADING_API_KEY, SPOT_TRADING_API_SECRET, tld='us')

# lookback is in seconds

# entry value 0.001 -> should have risen by 0.1%
def btc_usdt_strategy(entry, lookback, qty, open_position=False):

    if not open_position:

        while True:

            look_back_period = btc_usdt_utils.get_lookback_period(lookback)
            print(look_back_period)
            cum_ret = btc_usdt_utils.get_cumulative_returns(look_back_period)

            print(cum_ret[cum_ret.last_valid_index()])
            print(entry)
            print('---------------------------------')

            if cum_ret[cum_ret.last_valid_index()] > entry:

                order = spot_trading_client.create_order(
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
            
            since_buy = btc_usdt_utils.get_price_data_since_buy(order['transactTime'])

            if len(since_buy) > 1:

                since_buy_ret = btc_usdt_utils.get_cumulative_returns(since_buy)
                last_entry = since_buy_ret[since_buy_ret.last_valid_index()]

                # add print for df
                print(last_entry, last_entry > 0.0002)

                if last_entry > 0.0002: # this means 0.02%

                    order = spot_trading_client.create_order(
                                                symbol='BTCUSDT',
                                                side='SELL',
                                                type='MARKET',
                                                quantity=qty                                                
                                               )
                    
                    print(order)
                    break
    
btc_usdt_strategy(0.0002, 300, 0.0001)
