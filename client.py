from websocket import create_connection
ws = create_connection("ws://artisvideo.com:8765/socket")
Text = input("Please gib me some text - ")
ws.send(Text)
print("Sent")
result =  ws.recv()
print("Received '%s'" % result)