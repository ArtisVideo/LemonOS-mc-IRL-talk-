import pymongo
import websocket

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1")

ws.send("Hello, World")

ws.close()