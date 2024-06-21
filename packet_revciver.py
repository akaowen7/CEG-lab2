import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 80))
serverSocket.listen(5)

while True:
  (clientSocket, address) = serverSocket.accept()
  print(clientSocket.recv(1024))