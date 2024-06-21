import sys
import socket

print(sys.argv)

# Send a websocket message to the server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 80))
clientSocket.send(b"Hello, world!")