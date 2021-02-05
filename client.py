from websocket import create_connection
ws = create_connection("ws://192.168.0.101:25565")
Text = input("Please gib me some text - ")
ws.send(Text)
print("Sent")
result =  ws.recv()
print("Received '%s'" % result)