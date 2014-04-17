import os,sys
from socket import *
import serverConfig

file = ''
class Server:
    gate = socket(AF_INET, SOCK_STREAM)   
    host = serverConfig.host
    client_socket=''
    def __init__(self, port):
        self.port = port
        self.gate.bind((self.host, self.port))  
        self.listen()

    def listen(self):
            print("Listening for connections, on PORT: ", self.port)
            self.gate.listen(1000)
            while True:
                self.client_socket,address = self.gate.accept()
                print("TCP Server received connect from: " + str(address))
                self.receiveFileName()
                self.receiveFile()


    def receiveFileName(self):
            data = self.client_socket.recv(1024).decode("utf-8", "ignore")
            self.file = data

    def receiveFile(self):
        createFile = open("new_"+self.file, "wb")
        while True:
            data = self.client_socket.recv(1024)
            if (data==b''):
                break
            print(data)
            createFile.write(data)
        createFile.close()
        if(sys.platform.startswith('win')):
            os.system("start"+"new_"+self.file)
        else:
            os.system("gnome-open "+"new_"+self.file) 
        

        
        
server= Server(serverConfig.port)
self.gate.close()