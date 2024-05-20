import socket

def receive_file(server_host, server_port, filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        data = client_socket.recv(1024)
        with open(filename, 'wb') as file:
            file.write(data)
        print(f"File received and saved as {filename}")

def main():
    server_host = 'localhost'
    server_port = 12345
    filename = 'received_file.txt'

    receive_file(server_host, server_port, filename)

if __name__ == "__main__":
    main()
