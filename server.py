# server code
import socket

# create server socket
server_socket = socket.socket()

# bind server socket to localhost and port
server_socket.bind(('localhost', 8000))

# listen to incoming clients
server_socket.listen(1)

# accept connection from client
client_socket, address = server_socket.accept()

# receive message from client
message = client_socket.recv(1024)

# process message
print(f"Received message from {address}: {message.decode()}")

# send message to client
response = "Thank you for your message"
client_socket.send(response.encode())

# close connection
client_socket.close()