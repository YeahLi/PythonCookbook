from socket import *

class User(object):
    def __init__(self, user_id, addr):
        super(User, self).__init__()
        self.user_id = user_id
        self.addr = addr
        self.is_online = True

user_id_list = [] #save user id
user_list=[] #save user instances

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAddr = ("", 7788)
    udpSocket.bind(bindAddr)
    while True:
        # 1. Receive data sending from client
        recvData, sourceInfo = udpSocket.recvfrom(1024)
        data = recvData.decode("utf-8").split(":") # data should looks like "source_user_id:msg:des_user_id"
        source_user_id = data[0]
        msg = data[1]
        des_user_id = data[2]
        addr = sourceInfo
        print("user_id:%s,msg:%s" %(source_user_id,msg))

        #2. Check the message sending from user
        #logon
        if msg=="logon" and source_user_id == des_user_id:
            print("User %s logon." %source_user_id)
            #add into user_list
            user = User(source_user_id, addr)
            if source_user_id not in user_id_list:
                user_id_list.append(source_user_id)
                user_list.append(user)
            for item in user_list:
                if item.user_id == source_user_id:
                    item.is_online=True
                    break

            #Respond back to the user and tell the user logon successfully
            sendAddress = addr
            sendData = "You have successfully logon."
            udpSocket.sendto(sendData.encode("utf-8"),sendAddress)
        #logoff
        elif msg=="logoff" and source_user_id == des_user_id:
            
            if source_user_id in user_id_list:
                for item in user_list:
                    #find the user in the list
                    if item.user_id == source_user_id:
                        item.is_online=False
                        sendAddress = addr
                        sendData = "You have already logoff."
                        udpSocket.sendto(sendData.encode("utf-8"),sendAddress)
                        break  
            else:
                sendAddress = addr
                sendData = "The user %s doesn't exit." %(source_user_id)
                udpSocket.sendto(sendData.encode("utf-8"),sendAddress)
            
        #send back user ip
        elif msg=="connect":
            #check if des_user_id is in the user list
            if des_user_id in user_id_list:
                for item in user_list:
                    if item.user_id == des_user_id:
                        sendAddress = addr
                        sendData=str(item.addr)
                        udpSocket.sendto(sendData.encode("utf-8"),sendAddress)
                        break
            else:
                sendAddress = addr
                sendData = "The user %s doesn't exit." %(des_user_id)
                udpSocket.sendto(sendData.encode("utf-8"),sendAddress)
        else:
            print("Invalid request")

    udpSocket.close()

if __name__ == '__main__':
    main()