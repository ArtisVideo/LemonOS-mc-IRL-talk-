while True:
    from websocket import create_connection
    ws = create_connection("ws://192.168.0.101:25565")
    message =  ws.recv()
    print(message)