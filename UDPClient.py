import socket
import threading

class UDPClient:

    def __init__(self, IPAddress, port):
        self.IPAddress = IPAddress
        self.port = port
        self.buffer_size = 2048
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.last_package = None

    def connect(self):
        try:
            self.client.bind((self.IPAddress, self.port))
            t = threading.Thread(target=self.listen)
            t.start()
        except:
            print("Error connecting to stream!")

    def close(self):
        try:
            self.client.shutdown()
            self.client.close()
        except:
            pass

    def listen(self):
        while True:
            self.last_package, client = self.client.recvfrom(self.buffer_size)
