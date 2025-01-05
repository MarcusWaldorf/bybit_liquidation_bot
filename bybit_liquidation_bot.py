import time
from pybit.unified_trading import WebSocket



ws = WebSocket(testnet=False, channel_type='linear')


# Get all elements from the list
coins = ['BTCUSDT','ADAUSDT']

# Decode bytes to strings
bybit_symbols = [item.decode('utf-8') for item in coins]


def handle_message(message):

    if 'topic' in message and 'ts' in message and 'data' in message:
        asset = message['topic'].replace(f'liquidation.', '')
        ts = message['ts']
        side = message['data']['side']
        size = message['data']['size']
        price = message['data']['price']
        vol_dol = float(size)*float(price)
        vol_dol = round(vol_dol,2)

        print(ts, asset, side, size, price, vol_dol)

        
# Websocket stream
ws.liquidation_stream(symbol=bybit_symbols, callback=handle_message)


while True:

    time.sleep(1)