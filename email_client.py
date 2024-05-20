import socket
client_socket=socket.socket()
client_socket.connect(('localhost',587))
name=input('Enter the data:')
data=name.encode('utf-8')
client_socket.send(data)
received_data=client_socket.recv(1024).decode('utf-8')
print(received_data)
