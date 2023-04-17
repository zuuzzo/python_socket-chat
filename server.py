import socket

HOST = ''  # The server's hostname or IP address
PORT = 54321  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection closed")
                    break
                print('Received:', data.decode())
                message = input('Enter your message: ')
                conn.sendall(message.encode())