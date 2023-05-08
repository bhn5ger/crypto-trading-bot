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

if __name__ == "__main__":

    df = get_data('BTCUSDT', '2023-01-01')
    df.resample('D').first().Open

    print(df)