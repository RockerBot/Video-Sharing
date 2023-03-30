import socket
import cv2 as cv
import pickle
import struct

KB = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # host_ip = '192.168.191.239'
    host_ip = '192.168.1.6'
    PORT = 10050
    client_socket.connect((host_ip, PORT))

    data = b""
    payload_size = struct.calcsize("Q?")

    while True:
        print('.')
        while len(data) < payload_size:
            print('20')
            packet = client_socket.recv(4*KB)
            print('22')
            if packet: 
                data += packet
                print('25')
            else: 
                break
        packed_msg_size = data[:payload_size]
        print('29')
        data = data[payload_size:]
        print('31')
        msg_size = struct.unpack("Q?", packed_msg_size)[0]
        print('33')
        while len(data) < msg_size:
            print('35')
            data += client_socket.recv(4*KB)
            print('37')
        frame_data = data[:msg_size]
        print('39')
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv.imshow("Receiving...", frame)
        key = cv.waitKey(10)
        if key == 13: break
    client_socket.close()