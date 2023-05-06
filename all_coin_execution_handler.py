import os
import all_coin_utils
from binance.client import Client 

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(API_KEY, API_SECRET, tld='us')

# lookback is in minutes

def all_coin_strategy(lookback):


    top_coin = all_coin_utils.get_coin_with_greatest_cumulative_returns_in_past_n_minutes(lookback)
    investment_amt = 300
    lot_size = all_coin_utils.get_minimum_permitted_investment_qty(top_coin)
    price = float(client.get_symbol_ticker(symbol=top_coin)['price'])
    buy_quantity = round(investment_amt/price, len(str(lot_size).split('.')[1]))

    print(price)

all_coin_strategy(6000)



    