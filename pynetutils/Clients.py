import socket
import sys


class Client:
    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port


class TCPClient(Client):
    def __init__(self, target_host, target_port):
        super().__init__(target_host, target_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connect()

    def _connect(self):
        self.socket.connect((self.target_host, self.target_port))

    def send(self, data, flags=None):
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.socket.send(data, flags)

    def recv(self, buffsize=4096):
        return self.socket.recv(buffsize)

    @classmethod
    def sender(cls, host, port):
        try:
            client = cls(host, port)
            buffer = input(">")
            client.send(buffer)
            while True:
                recv_len = 1
                response = b""
                while recv_len:
                    data = client.recv()
                    recv_len = len(data)
                    response += data
                    if recv_len < 4096:
                        break
                print(response)
                buffer = input(">")
                client.send(buffer)
        except:
            print("[*] Exception occurred while connecting!")
            print("[*] Exiting...")
            sys.exit(-1)


class UDPClient(Client):
    def __init__(self, target_host, target_port):
        super().__init__(target_host, target_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.socket.sendto(data, (self.target_host, self.target_host))

    def recv(self, buffsize=4096):
        return self.socket.recvfrom(buffsize)[0]