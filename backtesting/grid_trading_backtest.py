import pandas as pd
from binance.client import Client

client = Client(tld='us')

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
    

def sliced_df(df, date):

    return df[df.index.date == pd.to_datetime(date).date()]  
 

if __name__ == "__main__":

    df = get_data('BTCUSDT', '2023-01-01')
    opens = df.resample('D').first().Open
    df_t = sliced_df(df, '2023-01-01')

    in_position = False

    for index, row in df_t.iterrows():

        #print(index, row)

        if not in_position:

            levels = get_levels(opens, '2023-01-01')

            print(row.Low, levels[0])

            if row.Low <= levels[0]:

                print('buy')
                in_position = True

        if in_position:

            if row.High >= levels[1]:

                print('sold')
                in_position = False

