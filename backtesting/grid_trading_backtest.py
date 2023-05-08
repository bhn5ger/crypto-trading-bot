import pandas as pd
from binance.client import Client

client = Client()

def get_data(symbol, start):

    frame = pd.DataFrame(client.get_historical_klines(symbol, '1m', start))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)

    return frame

def get_levels(opens, date, first=True):
    
    if first:
        return opens[date] * 0.998, opens[date] * 1.002
    else:
        return opens[date] * 0.996, opens[date] * 0.998
    

if __name__ == "__main__":

    df = get_data('BTCUSDT', '2023-01-01')
    opens = df.resample('D').first().Open

    print(get_levels(opens, '2023-01-01'))