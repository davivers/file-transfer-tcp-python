import socket

sock = socket.socket()
server = ('127.0.0.1', 4448)
sock.bind((server))
sock.listen(1)  #listen() specifies that the connection is formed through TCP protocols.

conn, addr = sock.accept()
print(f'{addr}' "Has connected to host.")

filename = input(str("Enter FileName"))   ##send data from a file with the specified name to the file the client required.
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been sent successfully")