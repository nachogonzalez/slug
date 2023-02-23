import socket
import keyboard
from loguru import logger



# Creation of a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Link to a particular address and port
server_address = ('localhost', 10000)
logger.info('Starting server on port {} {}'.format(*server_address))
sock.bind(server_address)

# Listening incoming connections
sock.listen(1)

while True:
    # Waiting for a connection
    logger.info('Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        logger.info('Connection from', client_address)

        # We receive data on packages and reassemble them
        while True:
            data = connection.recv(16)
            logger.info('Received {!r}'.format(data))
            if data:
                logger.info('Sending data back to the client')
                connection.sendall(data)
            else:
                logger.info('No more data', client_address)
                break
            
    finally:
        # Closing connection
        connection.close()