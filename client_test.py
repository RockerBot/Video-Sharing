# import socket
# import cv2 as cv
# import pickle
# import struct
# # import imutils

# KB = 1024

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_ip = '192.169.51.48'
# # host_ip = '192.168.51.239'
# port = 10050
# client_socket.connect((host_ip, port))
# print("Connected!")

# data = b""
# payload_size = struct.calcsize("Q")

# while True:
#     while len(data) < payload_size:
#         packet = client_socket.recv(4*KB)
#         if packet: data += packet
#         else: break
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack("Q", packed_msg_size)[0]
#     while len(data) < msg_size:
#         data += client_socket.recv(4*KB)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]
#     frame = pickle.loads(frame_data)
#     cv.imshow("Receiving...", frame)
#     key = cv.waitKey(10)
#     if key == 13: break
# client_socket.close()



import socket
import time

HEADER = 64
PORT = 19699
FORMAT = 'utf-8'
SERVER = "192.168.17.173" #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

i = 0
while i<100:
    send("REDPC apple")
    time.sleep(2)
    i += 1
send("REDPC orange")
send(DISCONNECT_MESSAGE)