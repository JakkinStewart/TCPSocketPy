import socket
import threading

bind_ip   = "0.0.0.0"
bind_port =[1024,1025,1026,1027,1028,1029,1030]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


for i in bind_port:
    server.bind((bind_ip, i))

server.listen(5)

#print("Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    request = client_socket.recv(4096)
    print("Received: %s" % request)
    client_socket.send("Fuck you!")
    client_socket.close()

while True:
    client,addr = server.accept()
    print("Accepted connection from %s:%d" % (addr[0],addr[1]))
    #client_handler = threading.Thread(target=handle_client, args=(client,))
    #client_handler.start()
