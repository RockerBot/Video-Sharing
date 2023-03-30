import socket


sender_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)

port = 10050

socket_address = (host_ip,port)
print('Socket created')
sender_sckt.bind(socket_address)
print('Socket bind complete')
sender_sckt.listen(5)
print('Socket now listening')



while True:
    client_socket, addr = sender_sckt.accept()
    print('Connection from:', addr)
    client_socket.sendall(65)
    client_socket.close()