# Python Network Programming

## 1. Basic Knowledges

### a. TCP/IP protocol group:
Application Layer: HTTP, SSL, FTP, SMTP ...
Transport Layer: TCP, UDP
Network Layer: IP, ICMP, IGMP, ARP, RARP
Link Layer

### b. Port
If a host is like a hotel, then the port is like door of a room.
Port 0-1023 is reserved for system services
Port 1024 - 65535 can be used for any program.

### c. IP Address
IP address is the location of a host.
127.0.0.1 is localhost, used for testing the network configuration on a host.

### d. 通讯术语
+ 单工 -- 只有一个人能说话，另一个人听着
+ 半双工 -- 同一时间只能有一个人说
+ 全双工 -- 相当于电话

网络是双全工的.

## 2. Socket

Sockets allow communication between two different processes on the same or different machines. To be more precise, it's a way to talk to other computers using standard Unix file descriptors. In Unix, every I/O action is done by writing or reading a file descriptor. A file descriptor is just an integer associated with an open file and it can be a network connection, a text file, a terminal, or something else.

To a programmer, a socket looks and behaves much like a low-level file descriptor. 

### a. Create a socket:
```python
import socket

#Create a tcp socket -- SOCK_STREAM
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create a udp socket -- SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

```

### b. Bind port with socket
If no port was specified to a socket, the program would get a random port.
```python
##If your host has more than one network interfaces, select one ip you need to bind.
bindAddr = ("", 7788)
s.bind(bindAddr)
```

### c. Send message
```python
sendAddr = ("192.168.1.5", 8085)
s.sendto(sendData.encode("utf-8"), sendAddr)
```

### d. Receive message
```python
bindAddr = ("", 7788)
s.bind(bindAddr)
while True:
		recvData, sourceInfo = s.recvfrom(1024) #every time receives 1024 bytes.
		print(reData.decode("utf-8"))
```
### e. Close socket
```python
s.close()
```

## 3. UDP Programming

<img src="./udp1.png" width="480" />

### a. Create UDP client
```python
from socket import *
#1. Create UDP socket
udpSocket = socket(AF_INET, SOCK_DGRAM)
#2. Prepare for accepter address
sendAddr = ("192.168.1.5", 8085)
#3. Prepare for send dat
sendData = "Hello, my name is Henry"
#4. Send to accepter:
udpSocket.sendto(sendData.encode("utf-8"), sendAddr)
#5. Close socket
udpSocket.close()
```
### b. Create UDP receiver
```python
from socket import *

def main():
	#1. Crete UDP socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	#2. Prepare bind information
	bindAddr = ("", 8080)
	#3. Bind IP and port to socket
	udpSocket.bind(bindAddr)
	#4. Call recvfrom() to receive message
	while True:
		recvData, sourceInfo = udpSocket.recvfrom(1024) #every time receives 1024 bytes.
		print(reData.decode("utf-8"))
	#5. Close socket
	udpSocket.close()
```

## 4. TCP Programming
<img src="./tcp1.png" width="350" />

### a. 