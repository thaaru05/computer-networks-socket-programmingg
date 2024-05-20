import socket

server_socket=socket.socket()
print('Socket Created')
server_socket.bind(('localhost',587))
server_socket.listen(3)
print('Socket is now listening')

while True:
    conn,addr=server_socket.accept()
    data=conn.recv(1024).decode('utf-8')
    print('Connected to',addr)
    print('Data:',data)
    conn.send(bytes('Welcome to local mail server','utf-8'))
    conn.close()



