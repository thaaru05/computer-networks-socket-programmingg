import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server is ready to receive")

expected_seq_num = 0

while True:
    data, client_address = server_socket.recvfrom(1024)
    seq_num, message = map(int, data.decode().split(","))
    #To check Go back N extra condition is used
    if seq_num == expected_seq_num and int(message) not in [11,12,13,14,15]:
        print("Received:", message)
        expected_seq_num += 1
        server_socket.sendto(str(expected_seq_num).encode(), client_address)
    else:
        print("Discarded:", message)
        server_socket.sendto(str(expected_seq_num).encode(), client_address)
