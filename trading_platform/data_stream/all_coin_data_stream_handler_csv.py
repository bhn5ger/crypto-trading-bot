import websocket
import json
import pandas as pd

path = '/home/briann.briannn/crypto-trading-bot/trading_platform/data_stream/csvs'

stream = "wss://stream.binance.com:9443/ws/!miniTicker@arr"

def on_message(ws, message):
    msg = json.loads(message)
    symbol = [x for x in msg if x['s'].endswith('USDT')]
    frame = pd.DataFrame(symbol)[['E','s','c']]
    frame.E = pd.to_datetime(frame.E, unit='ms')
    frame.c = frame.c.astype(float)

ws = websocket.WebSocketApp(stream, on_message=on_message)
ws.run_forever()
