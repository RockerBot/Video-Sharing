import socket
import cv2 as cv
import pickle
import struct
# import imutils

KB = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # host_ip = '192.168.191.239'
    host_ip = '10.14.142.191'
    PORT = 10050
    client_socket.connect((host_ip, PORT))

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