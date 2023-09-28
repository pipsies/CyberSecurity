import socket

#creating socket object
serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 444 

#binding to socket
serversocket.bind((host, port)) #Host will be replaces/substituted with IP, if changed and not runing on host

#Start TCP listener
serversocket.listen(3)


while True:
    #Starting the Connection
    clientsocket, address = serversocket.accept()
    print("Connection has been established from " &str(address))

    message = "Hello!, Thank you for connecting to the server" + "\r\n"
    clientsocket.send(message)
    clientsocket.close() 