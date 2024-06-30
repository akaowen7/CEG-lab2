import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 80))
serverSocket.listen(5)

while True:
  (clientSocket, address) = serverSocket.accept()
  data = clientSocket.recv(1024).hex()

  if data != '':
    header = data[:40]
    message = data[40:]

    # split header into 4 byte hex values
    hex_header = [header[i:i+4] for i in range(0, len(header), 4)]
    check_sum = hex_header[5]
    hex_header.pop(5)

    # add hex values together excluding the 6th one(thats the check sum)
    sum = 0
    for hexStr in hex_header:
      sum += int(hexStr, 16)
    
    hex_sum = str(hex(sum))[2:]

    #add overflow to the sum
    if len(hex_sum) > 4:
      sum = int(hex_sum[1:], 16) + int(hex_sum[0], 16)
      hex_sum = hex(sum)
    
    # get the ones complement of the hex_sum
    ones_complement = str(hex(0xFFFF - int(hex_sum, 16)))[2:]

    # check if the check sum is correct
    if ones_complement == check_sum:
      print(message)
      break
    else:
      print('Check sum failed')
      break