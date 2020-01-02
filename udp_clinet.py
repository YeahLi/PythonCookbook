from socket import *

#1. Create socket
udpSocket = socket(AF_INET, SOCK_DGRAM)
#2. Prepare for accepter address
sendAddr = ('192.168.1.5', 7788)
#3. Prepare for send data
sendData = "Hello, this is henry"
#4. Send to accepter
udpSocket.sendto(sendData.encode("utf-8"),sendAddr)
#5. Close socket
udpSocket.close()

#one socket is one file descriptor