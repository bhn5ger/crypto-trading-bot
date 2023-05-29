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
    

def sliced_df(df, date):

    return df[df.index.date == pd.to_datetime(date).date()]  
 

if __name__ == "__main__":

    # TODO: Parameterize date

    df = get_data('BTCUSDT', '2023-01-02')

    opens = df.resample('D').first().Open
    df_t = sliced_df(df, '2023-01-02')

    position_arr = [False, False]

    # Intraday

    '''

    for index, row in df_t.iterrows():

        if not position_arr[0]:

            first_levels = get_levels(opens, '2023-01-02') 
            second_levels = get_levels(opens, '2023-01-02', False)

            if row.Low <= first_levels[0]:
                print('buy')
                position_arr[0] = True

        if position_arr[0] and not position_arr[1]:

            if row.Low <= second_levels[0]:
                print('buy second')
                position_arr[1] = True

            if row.High >= first_levels[1]:
                print('sell')
                position_arr[0] = False

        if position_arr[1]:

            if row.High >= second_levels[1]:
                print('sell second')
                position_arr[1] = False

    '''

    # Interday

    position_arr = [False, False]
    profits = []


    for date in opens.index:
        
        df_t = sliced_df(df, date)

        if not any(position_arr): # only pull grid levels while not in open position
            first_levels = get_levels(opens, date) 
            second_levels = get_levels(opens, date, False)

        for index, row in df_t.iterrows():

            if not position_arr[0]:

                if row.Low <= first_levels[0]:
                    print('buy', index)
                    position_arr[0] = True
                    buy_1 = first_levels[0]

            if position_arr[0] and not position_arr[1]:

                if row.Low <= second_levels[0]:
                    print('buy second', index)
                    position_arr[1] = True
                    buy_2 = second_levels[0]

                if row.High >= first_levels[1]:
                    print('sell', index)
                    position_arr[0] = False
                    profits.append( (first_levels[1] - buy_1) / buy_1 )

            if position_arr[1]:

                if row.High >= second_levels[1]:
                    print('sell second', index)
                    position_arr[1] = False
                    profits.append( (second_levels[1] - buy_2) / buy_2 )

    # print(profits)
    