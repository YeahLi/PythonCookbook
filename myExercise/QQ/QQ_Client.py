from socket import *
from threading import Thread

ip = "192.168.1.5"
port = 17799
user_id = "henryli"

def logon(udpSocket):
	#send logon request
	sendData = "%s:logon:%s" %(user_id,user_id)
	sendAddr = ('192.168.1.5', 7788)
	udpSocket.sendto(sendData.encode("utf-8"),sendAddr)

	#receive logon response
	recvData, sourceInfo = udpSocket.recvfrom(1024) # 1024 表示本次接收最大字节数
	print(recvData.decode("utf-8"))

def logoff(udpSocket):
	#send logoff request
	sendData = "%s:logoff:%s" %(user_id,user_id)
	sendAddr = ('192.168.1.5', 7788)
	udpSocket.sendto(sendData.encode("utf-8"),sendAddr)

	#receive logoff response
	recvData, sourceInfo = udpSocket.recvfrom(1024) # 1024 表示本次接收最大字节数
	print(recvData.decode("utf-8"))

def getDestAddr(udpSocket, des_user_id):
	'''Get the address of des_user'''
	sendData = "%s:connect:%s" %(user_id,des_user_id)
	sendAddr = ('192.168.1.5', 7788)
	udpSocket.sendto(sendData.encode("utf-8"),sendAddr)
	recvData, sourceInfo = udpSocket.recvfrom(1024) # 1024 表示本次接收最大字节数
	return eval(recvData.decode("utf-8"))

def sendMsg(udpSocket,des_addr,msg):
	sendData = msg
	sendAddr = des_addr
	udpSocket.sendto(sendData.encode("utf-8"),sendAddr)

def receiveMsg(udpSocket,des_addr):
	while True:
		recvData, sourceInfo = udpSocket.recvfrom(1024) # 1024 表示本次接收最大字节数
		msg=recvData.decode("utf-8")
		if msg == "Hello!":
			sendMsg(udpSocket,sourceInfo,"hehe")
	

def main():
	#1. Create socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind((ip, port))
	#2. logon
	logon(udpSocket)
	#3. connect to another user
	#a. get the destination addr
	des_addr = getDestAddr(udpSocket,"whitney")
	print("%s" %str(des_addr))
	#b. send msg
	ts = Thread(target=sendMsg,args=(udpSocket,des_addr,"Hello!"))
	ts.start()
	#c. receive msg
	tr = Thread(target=receiveMsg, args=(udpSocket,des_addr))
	tr.start()
	#5. Close socket
	ts.join()
	tr.join()
	udpSocket.close()


#one socket is one file descriptor

if __name__ == '__main__':
	main()