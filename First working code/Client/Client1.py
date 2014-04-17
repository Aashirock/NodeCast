from socket import *
class Client:
    
    gateway = socket(AF_INET, SOCK_STREAM)
    def __init__(self, host,port, file):
        self.port = port
        self.host = host
        self.file = filename
        self.connect()

    def connect(self):
        self.gateway.connect((self.host, self.port))
        self.sendFileName()
        self.sendFile()

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

client= Client(host,port,filename)

