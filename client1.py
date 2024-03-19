import socket
import sys

server_address = ('localhost', 5000)

try:
    while True:

        print("input message")
        strsend = input("message :")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)

        client_socket.send(strsend.encode())
        data = client_socket.recv(1024).decode()

        print(str(data))

        client_socket.close()
except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)