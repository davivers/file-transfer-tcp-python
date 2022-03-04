import socket

sock = socket.socket()
server = ('127.0.0.1', 4448)
sock.connect(server)

filename = input(str("Enter filename"))
file = open(filename, 'wb')
file_data = sock.recv(1024)
file.write(file_data)
file.close()
print("File has been received.")