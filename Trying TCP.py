#Imports
import socket
import sys

#Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#create server
server_address = ('localhost', 1337)
sock.bind(server_address)

#Print incoming connections
sock.listen(1) #Listen for incomming connections
while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(160)

            DataGud = data.decode('UTF-8')
            print(DataGud)

    #Close connecction      
    finally:
        connection.close()