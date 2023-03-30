import socket
import cv2 as cv
import pickle
import struct
import threading

running = False
KB = 1024
clients = {} # ip: client_sckt
streams = {} # ip: video data


def broadcast_stream():
    while running:
        for frm_client in clients:
            if not (stream:=streams.get(frm_client)):continue
            a = pickle.dumps(stream)
            message = struct.pack("Q", len(a))+a
            for to_client in clients:
                if to_client is frm_client: continue
                clients[to_client].sendall(message)


def manage_client(client_sckt, client_address,/):
    print(f'New Client: {client_address[0]} {client_address[1]}')
    client_sckt.send(str.encode('Server is working:'))
    clients[client_address] = client_sckt
    data = b""
    payload_size = 9#struct.calcsize("Q?")
    while clients.get(client_address):
        data += client_sckt.recv(4 * KB)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size, is_online = struct.unpack("Q?", packed_msg_size)
        if not is_online: clients[client_address] = None
        while len(data) < msg_size:
            data += client_sckt.recv(4 * KB)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        streams[client_address] = frame
    client_sckt.close()




def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sckt:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print(f'HOST NAME:{host_name}[{host_ip}]')
        PORT = 10050
        socket_address = (host_ip, PORT)
        print('Socket created')
        server_sckt.bind(socket_address)
        print('Socket Bound')
        server_sckt.listen(5)
        print('Socket now listening')
        threading.Thread(target=broadcast_stream).start()
        while running:
            client_socket, client_address = server_sckt.accept()
            threading.Thread(target=manage_client, args=(client_socket, client_address)).start()


if __name__ == "__main__":
    running = True
    run_server()