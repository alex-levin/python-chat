import socket 
import threading

class ClientSocket:
    def __init__(self):
        # https://docs.python.org/3.8/library/socket.html
        # socket.AF_INET means socket belongs to IPV4 Family
        # socket.SOCK_STREAM means connection configured using TCP Protocol
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.sock.connect(port_and_ip)

    # This single line method it used to send a SMS to the connected client, the message must be in bytes during
    # transmission thus why we have used encode() method on our string
    def send_message(self, message):
        self.sock.send(message.encode())

    # This method is used to receive the message from the client through out the program life.
    # It will be threaded to prevent the app from freezing.
    def receive_message(self):
        while True:       
            data = self.sock.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            message = input()
            self.send_message(message)

csocket = ClientSocket()
# __init__(csocket) is called implicitly
always_receive = threading.Thread(target=csocket.receive_message)
always_receive.daemon = True
always_receive.start()
csocket.main()