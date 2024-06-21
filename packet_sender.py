import sys
import socket
from Hex import HexVal

def groupHex(hexList):
    groupedHex = []
    for i in range(0, len(hexList), 2):
        groupedHex.append(str(hexList[i][2:]) + str(hexList[i + 1][2:]))
    return groupedHex

print(sys.argv)

# Send a websocket message to the server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 80))
clientSocket.send(b"Hello, world!")

serverAddress = sys.argv[2]
payload = sys.argv[4]

hexPayload = []
for i in payload:
    hexPayload.append(hex(ord(i)))

hexPayloadGrouped = groupHex(hexPayload)

header = ['4500', '0028', '1c46', '4000', '4006', '0000']

hexServerAddress = []
for i in serverAddress.split('.'):
    hexServerAddress.append(hex(int(i)))

hexServerAddressGrouped = groupHex(hexServerAddress)

header.append(hexServerAddressGrouped[0])
header.append(hexServerAddressGrouped[1])

