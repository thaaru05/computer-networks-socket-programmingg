import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
window_size = 3
total_messages = 10

print("Client is ready to send")

base = 0
seq_num = 0

while base < total_messages:
    for seq_num in range(base, min(base + window_size, total_messages)):
        message = input("Enter Messages (Number) : ")
        print(f'Sending: {message} with Seq_num {seq_num}')
        client_socket.sendto(f"{seq_num},{message}".encode(), server_address)
        #Extra condtion to receive random acknowledgement 
        if int(message) in [1, 2, 3, 4, 5]:
            break

    for _ in range(base, seq_num + 1):
        ack = client_socket.recv(1024).decode()
        print("Received acknowledgment:", ack)
        base = int(ack)


client_socket.close()
