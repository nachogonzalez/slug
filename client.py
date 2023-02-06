# client code
import socket

# create client socket
client_socket = socket.socket()

# connect to server
client_socket.connect(('localhost', 8000))

# send message to server
message = "Hello from the client!"
client_socket.send(message.encode())

# receive message from server
response = client_socket.recv(1024)