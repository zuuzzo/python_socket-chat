import socket

HOST = ''  # The server's hostname or IP address
PORT = 54321  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter your message: ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received:', data.decode())