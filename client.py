import socket
import cv2 as cv
import pickle
import struct
# import imutils

KB = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_ip = '192.169.51.48'
host_ip = '192.168.191.48'
# host_ip = '192.168.216.219'
# host_ip = socket.gethostbyname(socket.gethostname())
port = 10050
client_socket.connect((host_ip, port))
print("Connected!")

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*KB)
        if packet: data += packet
        else: break
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    while len(data) < msg_size:
        data += client_socket.recv(4*KB)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv.imshow("Receiving...", frame)
    key = cv.waitKey(10)
    if key == 13: break
client_socket.close()


# import socket
# HOST = '192.168.51.48'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))