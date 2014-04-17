import os
from socket import *

class NodeOne:
    
    gateway = socket(AF_INET, SOCK_STREAM)
    def __init__(self, host,port):
        self.port = port
        self.host = host
        

    def connect(self):
        self.gateway.connect((self.host, self.port))

    def sendFileName(self,file):
        self.gateway.send((file).encode("utf-8","ignore"))

    def sendFile(self,file):

        readByte = open(file, "rb")
        data = readByte.read()
        readByte.close()

        self.gateway.sendall(data)
        
        


i=1
host=input("Enter the host IP Address you wanna show the file::")
port=int(input("Enter the port number::"))
filename=input("Enter the file name you wanna send::")
nodeOne= NodeOne(host,port)
nodeOne.connect()
while(i<=5):
    print("Taking screenshot::"+str(i))
    filename=filename+str(i)+".jpg"
    os.system("scrot "+filename)
    nodeOne.sendFileName(filename)
    nodeOne.sendFile(filename)
    i=i+1
    filename='screenshot'
nodeOne.gateway.close()
