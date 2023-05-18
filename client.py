import os
import time
import hashlib
from socket import *

# set up client
serverName = '3.91.247.83'
serverPort = 8181
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# receive file and checksum
filedata = clientSocket.recv(1024)
checksum = clientSocket.recv(1024).decode()

# save received file in /clientdata directory
with open('/clientdata/received_file.txt', 'wb') as f:
    f.write(filedata)

# verify checksum
with open('/clientdata/received_file.txt', 'r') as f:
    data = f.read()
    computed_checksum = hashlib.md5(data.encode()).hexdigest()
    if computed_checksum == checksum:
        print('Checksums match')
    else:
        print('Checksums do not match')



while True:
    time.sleep(1) 

clientSocket.close()

