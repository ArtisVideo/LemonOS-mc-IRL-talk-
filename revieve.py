while True:
    from websocket import create_connection
    ws = create_connection("ws://localhost:8765")
    message =  ws.recv()
print(message)