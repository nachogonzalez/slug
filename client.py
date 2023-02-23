import socket
import toolbox
from loguru import logger

# Agent initialization
id = toolbox.generateID()
logger.info("Agent id: " + id)
logger.info("Agent geo info: " + toolbox.getGeoInfo())

# Creation of a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We connect the socket to the server
server_address = ('localhost', 10000)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    
    # Send data
    message = 'Test message - Lorem ipsum'
    logger.info('Sending {!r}'.format(message))
    sock.sendall(message.encode('utf-8'))

    # Look for response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logger.info('Received {!r}'.format(data))

finally:
    logger.info('Closing the socket')
    sock.close()