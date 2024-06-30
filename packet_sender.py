import sys
import socket

# Group hex values into 2-byte chunks
def groupHex(hexList):
    groupedHex = []
    for i in range(0, len(hexList), 2):
        # If the hex value is less than 16, add a 0 to the front
        if len(hexList[i]) == 3:
            hexList[i] = '0x0' + hexList[i][2]
        if len(hexList[i + 1]) == 3:
            hexList[i + 1] = '0x0' + hexList[i + 1][2]

        # Combine the two hex values into one string
        groupedHex.append(str(hexList[i][2:]) + str(hexList[i + 1][2:]))
    return groupedHex

# Send a websocket message to the server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 80))
# clientSocket.send(b"Hello, world!")

# Pull address and payload from command line arguments
serverAddress = sys.argv[2]
payload = sys.argv[4]

# Translate Payload to Hex
hexPayload = []
for i in payload:
    hexPayload.append(hex(ord(i)))

hexPayloadGrouped = groupHex(hexPayload)


# Create header
header = ['4500', '0028', '1c46', '4000', '4006', '0000']

# Translate server address to hex 
hexServerAddress = []
for i in serverAddress.split('.'):
    hexServerAddress.append(hex(int(i)))

print(hexServerAddress)

hexServerAddressGrouped = groupHex(hexServerAddress)

header.append(hexServerAddressGrouped[0])
header.append(hexServerAddressGrouped[1])
header.append('c0a8') # This is just 192.168.0.1 in hex
header.append('0001') # We might not want to hard-code this...


#           Calculate checksum
# Sum all packets in the header
checksum = hex(0)
for i in header:
    checksum = hex(int(checksum, 16) + int(i, 16))

# Check for overflow
if int(checksum, 16) > int('FFFF', 16):
    firstDigit = int(checksum[2])
    checksum = hex(int(checksum, 16) - int(str(firstDigit) + '0000', 16) + firstDigit)

# One's Complement
checksum = hex(int('FFFF', 16) - int(checksum, 16))

header[5] = checksum[2:]

# Send the packet (Not sure how this works)
clientSocket.send(bytes.fromhex(''.join(header) + ''.join(hexPayloadGrouped)))