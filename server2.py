import socket
import sys
import datetime

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)


try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(client_socket, client_address)

        timestamp = datetime.datetime.now()

        data = client_socket.recv(1024).decode()
        print(str(data))
        logfile = open('logfile.log', 'a')

        log = str(timestamp) + str(client_address) + str(data)
        print(log)
        logfile.write(log)
        logfile.close()

        
        
        if data == "asklog":
            a = open("logfile.log", "r")
            response = a.read()
            
            a.close()
        else :
            response = log
        client_socket.send(response.encode())
        
        client_socket.close()

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)