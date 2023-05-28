import websocket
import json
import pandas as pd

def on_message(ws, message):
    msg = json.loads()

ws = websocket.WebSocketApp(stream, on_message=on_message)
ws.run_forever()