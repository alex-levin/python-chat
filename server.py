import socket 
import threading

class ServerSocket:
    def __init__(self):
       # https://docs.python.org/3.8/library/socket.html
        # socket.AF_INET means socket belongs to IPV4 Family
        # socket.SOCK_STREAM means connection configured using TCP Protocol
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        # Client socket must use exactly the same server IP and port in order to connect
        self.sock.bind(port_and_ip)
        # 5 is the number of unaccepted connections that the system will allow before refusing new connections.
        # If not specified, a default reasonable value is chosen.
        self.sock.listen(5)
        # The return value is a pair (conn, address) where conn is a new socket object usable to send and receive
        # data on the connection, and address is the address bound to the socket on the other end of the connection.
        self.connection, addr = self.sock.accept()

    def send_message(self, message):
        self.connection.send(message.encode())

    # This method is used to receive the message from the client through out the program life.
    # It will be threaded to prevent the app from freezing.
    def receive_message(self):
        while True:
            data = self.connection.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            message = input()
            self.send_message(message)

ssocket = ServerSocket()
# __init__(ssocket) is called implicitly
always_receive = threading.Thread(target=ssocket.receive_message)
always_receive.daemon = True
always_receive.start()
ssocket.main()