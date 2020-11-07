# Importing socket module 
import socket

print('Welcome to the server!')

# Creating a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# Reserved the port
port = 8000

# Binding server to the specified port
s.bind((socket.gethostname(), port))

# Putting the socket into listening mode 
s.listen(5)
print("Socket is listening")

while True:
	# Establishing connection with client 
	clientsocket, address = s.accept()
	print(f'Connection established with {address}')

	# Sending message to the client  
	clientsocket.send(bytes('Thank you for connecting to the server!', 'utf-8'))
	
