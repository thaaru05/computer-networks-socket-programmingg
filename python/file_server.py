import socket

def send_file(conn, filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            conn.sendall(data)
    except FileNotFoundError:
        print("File not found")

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

        filename = 'example.txt'
        send_file(conn, filename)

if __name__ == "__main__":
    main()
