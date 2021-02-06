#Imports
import socket
import sys

#Defune socket stuffs
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to server
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    
    # Send data
    msg = input("Please enter text to be sent")
    sock.sendall(msg)

finally:
    print("Closing socket...")
    sock.close()