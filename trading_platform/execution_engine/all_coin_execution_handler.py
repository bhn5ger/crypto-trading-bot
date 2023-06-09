import os, asyncio
import pandas as pd
import sys
sys.path.insert(1, '../utils')
import all_coin_utils, account_utils
from binance.client import Client 
from binance import AsyncClient, BinanceSocketManager


API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

SPOT_TRADING_API_KEY = os.environ.get('spot_trading_binance_api')
SPOT_TRADING_API_SECRET = os.environ.get('spot_trading_binance_secret')

client = Client(API_KEY, API_SECRET)
spot_trading_client = Client(SPOT_TRADING_API_KEY, SPOT_TRADING_API_SECRET, tld='us')
# lookback is in minutes

def all_coin_strategy(lookback, investment_amt):

    # TO-DO: Try-catch blocks for top_coin, buyprice, buy_quantity

    top_coin = all_coin_utils.get_coin_with_greatest_cumulative_returns_in_past_n_minutes(lookback)
    lot_size = all_coin_utils.get_minimum_permitted_investment_qty(top_coin)
    free_usd = account_utils.get_available_balance('USDT')
    
    print("top_coin:", top_coin)
    print("lot_size:", lot_size)
    print("free_usd:", free_usd)

    price = float(client.get_symbol_ticker(symbol=top_coin)['price'])
    buy_quantity = round(investment_amt/price, len(str(lot_size).split('.')[1]))

    print("price of top coin:", price)
    print("buy_quantity of top coin:", buy_quantity)

    print("Buy if my balance,", float(free_usd), "is greater than the investment amount,", investment_amt)

    if float(free_usd) > investment_amt:

        order = spot_trading_client.create_order(
                                    symbol=top_coin, 
                                    side='BUY',
                                    type='MARKET',
                                    quantity=buy_quantity
                                   )

        print("Order:", order)
        buyprice = float(order['fills'][0]['price'])
        print("Top coin buy price:", buyprice)

        return top_coin, buyprice, buy_quantity
        
    else:
        return None, None, None
    
def create_frame(msg):

    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df

async def main(coin, buyprice, buy_quantity):

    client_ = await AsyncClient.create()

    bm = BinanceSocketManager(client_)
    ts = bm.trade_socket(coin)

    async with ts as tscm:
        while True:
            msg = await tscm.recv()
            if msg:
                frame = create_frame(msg)
                print("Sell if", frame.Price[0], "the price of", coin, "is greater than", 1.001 * buyprice)
                if frame.Price[0] > 1.001 * buyprice:
                    order = spot_trading_client.create_order(
                                                symbol=coin,
                                                side='SELL',
                                                type='MARKET',
                                                quantity=buy_quantity
                                               )
                    loop.stop()

    await client.close_connection()
    

if __name__ == "__main__":

    '''
    top_coin: ETHUSDT
    lot_size: 0.0001
    free_usd: 98.02801345
    price of top coin: 1893.94
    buy_quantity of top coin: 0.0016
    Buy if my balance, 98.02801345 is greater than the investment amount, 3
    Order: {'symbol': 'ETHUSDT', 'orderId': 892181217, 'orderListId': -1, 'clientOrderId': 'WirUWY4UnB156vf4mY21bH', 
    'transactTime': 1685391976044, 'price': '0.00000000', 'origQty': '0.00160000', 'executedQty': '0.00160000', 
    'cummulativeQuoteQty': '3.03051200', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 
    'workingTime': 1685391976044, 'fills': [{'price': '1894.07000000', 'qty': '0.00160000', 
    'commission': '0.00000000', 'commissionAsset': 'BNB', 'tradeId': 15184291}], 
    'selfTradePreventionMode': 'EXPIRE_MAKER'}
    Top coin buy price: 1894.07
    Sell if 1893.94 the price of ETHUSDT is greater than 1895.9640699999998
    Sell if 1893.94 the price of ETHUSDT is greater than 1895.9640699999998
    Sell if 1893.94 the price of ETHUSDT is greater than 1895.9640699999998
    **JSON of sell order when ETHUSDT is greater than 1895.9640699999998**
    '''
    
    top_coin, buyprice, buy_quantity = all_coin_strategy(1, 3) # Identify the coin with the greatest cumulative returns in the past minute and buy $3 worth of it. 

    if top_coin and buyprice and buy_quantity:
        loop = asyncio.get_event_loop()
        msg = loop.run_until_complete(main(top_coin, buyprice, buy_quantity))
