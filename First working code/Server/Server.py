from socket import *
port = 5007
file = ''
class Server:
    gate = socket(AF_INET, SOCK_STREAM)   
    host = '127.0.0.1'
    client_socket=''
    def __init__(self, port):
        self.port = port
        self.gate.bind((self.host, self.port))  
        self.listen()

    def listen(self):
        self.gate.listen(10)
        while True:
            print("Listening for connections, on PORT: ", self.port)
            while True:
                self.client_socket,address = self.gate.accept()
                print("TCP Server received connect from: " + str(address))
                self.receiveFileName()
                self.receiveFile()

    def receiveFileName(self):
            data = self.client_socket.recv(1024).decode("utf-8", "ignore")
            self.file = data
            print("Received file name::"+self.file)

    def receiveFile(self):
        createFile = open("new_"+self.file, "wb")
        while True:
            data = self.client_socket.recv(1024)
            if (data==b''):
                break
            print(data)
            createFile.write(data)
        createFile.close()
        self.client_socket.close()
        
server= Server(port)
