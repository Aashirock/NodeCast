import os
from socket import *
class NodeTwo:
    
    gateway = socket(AF_INET, SOCK_STREAM)
    def __init__(self, host,port, file):
        self.port = port
        self.host = host
        self.file = filename
        

    def connect(self):
        self.gateway.connect((self.host, self.port))

    def sendFileName(self):
        self.gateway.send((self.file).encode("utf-8","ignore"))

    def sendFile(self):
        
        readByte = open(self.file, "rb")
        data = readByte.read()
        readByte.close()

        self.gateway.sendall(data)
        self.gateway.close()

host=input("Enter the host IP Address you wanna show the file::")
port=int(input("Enter the port number::"))
filename=input("Enter the file name you wanna send::")
filename=filename+".jpg"
os.system("scrot "+filename)
nodeTwo= NodeTwo(host,port,filename)
nodeTwo.connect()
nodeTwo.sendFileName()
nodeTwo.sendFile()

