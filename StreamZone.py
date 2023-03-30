import socket
import cv2 as cv
import pickle
import struct
import pygame # TODO
# import imutils

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
    # client_socket, addr = sender_sckt.accept()
    # print('Connection from:', addr)
    if client_socket:
        vid = cv.VideoCapture(0)
        while vid.isOpened():
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a))+a
            client_socket.sendall(message)
            cv.imshow('sending...', frame)
            key = cv.waitKey(10)
            if key == 13:
                client_socket.close()