import websocket

ws = websocket.WebSocket()
ws.connect("wss://artisvideo.com")

ws.send("Hello, World")

ws.close()