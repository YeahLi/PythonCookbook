from socket import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAddr = ("", 7788)
    udpSocket.bind(bindAddr)
    while True:
        recvData, sourceInfo = udpSocket.recvfrom(1024) # 1024 表示本次接收最大字节数
        print(recvData.decode("utf-8"))
        pass

    udpSocket.close()

if __name__ == '__main__':
    main()