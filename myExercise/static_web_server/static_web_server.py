from socket import *
from multiprocessing import Process

HTML_ROOT_DIR = "./html"

def fun(client_socket, client_address):
    # Receive request
    recvData = client_socket.recv(1024)
    if len(recvData) > 0:
        # Analyze request
        recvStr = recvData.decode("utf-8").splitlines()
        path = HTML_ROOT_DIR + recvStr[0].split(" ")[1]
        print(path)
        # Generate response
        try:
            with open(path, 'r') as f:
                responseData = f.read()
                responseStr = "HTTP1.1 200 OK\r\n\r\n" + responseData
                client_socket.send(responseStr.encode("utf-8"))
        except IOError:
            # response 404
            responseStr = "HTTP1.1 404 Page Not Found\r\n"
            client_socket.send(responseStr.encode("utf-8"))

    # close socket
    client_socket.close()


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    server_socket.bind(('', 7788))
    server_socket.listen(5)
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            p = Process(target=fun, args=(client_socket, client_address))
            p.start()
            client_socket.close()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
