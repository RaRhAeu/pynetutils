import socket
import subprocess
from threading import Thread


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


class TCPServer(Server):
    def __init__(self, ip, port, upload_dst=None, execute=None, command=None):
        super().__init__(ip, port)
        self.upload_dst = upload_dst
        self.execute = execute
        self.command = command
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._bind()

    def _bind(self):
        self.server.bind((self.ip, self.port))

    @staticmethod
    def run_command(command):
        command = command.rstrip()
        try:
            output = subprocess.check_output(command,
                                             stderr=subprocess.STDOUT,
                                             shell=True)
        except:
            output = b"Failed to execute command"
        return output

    def client_handler(self, client_socket):
        if self.upload_dst:
            file_buff = b''
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                else:
                    file_buff += data
            try:
                with open(self.upload_dst, 'wb') as f:
                    f.write(file_buff)
                client_socket.send(f"Successfully saved file to {self.upload_dst}".encode('utf-8'))
            except:
                client_socket.send(f"Failed to save file to {self.upload_dst}".encode('utf-8'))
        if self.execute:
            output = self.run_command(self.execute)
            client_socket.send(output)
        if self.command:
            client_socket.send(b"$> ")
            cmd_buff = client_socket.recv(1024)
            response = self.run_command(cmd_buff)
            client_socket.send(response)
        else:
            request = client_socket.recv(4096)
            try:
                request = request.decode('utf-8')
            except UnicodeError:
                pass

            print(f"[*] Received: {request}")
            client_socket.send(b"ACK!")
            client_socket.close()
            self.server.close()

    def accept(self):
        while True:
            client, addr = self.server.accept()
            print(f"[*] Connection received from: {addr[0]}:{addr[1]}")
            client_handler = Thread(target=self.client_handler, args=(client,))
            client_handler.start()

    @classmethod
    def server_loop(cls, host, port, upload_dst=None, execute=None, command=None, n_listen=5):
        tcp_server = cls(host, port, upload_dst, execute, command)
        tcp_server.server.listen(n_listen)
        tcp_server.accept()
