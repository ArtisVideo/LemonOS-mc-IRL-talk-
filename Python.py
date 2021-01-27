#Imports
from websocket_server import WebsocketServer

#New client print
def new_client(client, server):
    print("New client id %d" % client['id'])

#Message recievd print 
def message_received(client, server, message):

    if message_received == "test":
        send_message = input ("message to send:")
        server.send_message_to_all(send_message)

    else:
	    print("Client(%d) : %s" % (client['id'], message))


#Port specify
PORT=6002

#Detection > Run functions
server = WebsocketServer(PORT, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)

#Loop server untill stopped
server.run_forever()

