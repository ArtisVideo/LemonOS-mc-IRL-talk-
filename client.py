while True:
    from websocket import create_connection
    ws = create_connection("ws://Oscar-PC:25565")
    #Text = input("Please gib me some text - ")
    Text = input("")
    ws.send(Text)
    #print("Sent")
    #result =  ws.recv()
    #sprint("Received '%s'" % result)
