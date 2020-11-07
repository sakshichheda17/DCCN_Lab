# Importing socket module 
import socket

# Creating a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to sever
s.connect((socket.gethostname(), 8000))

# Receiving data from the server 
msg = s.recv(1024)

# Printing the received data
print(msg.decode('utf-8'))