import socket
import cv2 as cv
import pygame
import time
from pygame import gfxdraw

running = True
dt = 0

# serv_ip = input("Enter Server IP: ") # Original
# serv_ip = socket.gethostbyname(socket.gethostname()) # Tempo
serv_ip = "192.168.1.6"

print(f"Connecting to {serv_ip}...")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 10050

try:
    # server_conn_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((serv_ip, port))
    print("Connected!")
    print(client_socket.recv(1024))
except TimeoutError as te:
    print("Server Inactive")
    quit(-1)

# time.sleep(2)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont('jetbrainsmononerdfontcompletemono', 32)
boldFont = pygame.font.SysFont('jetbrainsmononlsemiboldnerdfontcompletemonowindowscompatible', 32)
width = screen.get_width()
height = screen.get_height()

# availStream = ['192.168.1.10']
availStream = {'192.168.1.10':'RED-PC','192.168.2.10':'BLUE-PC'}

n = 100
i = 3

while running:
    clientIP = [x for x in availStream.keys()]
    clientName = [x for x in availStream.values()]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    
    streamText = font.render('Available Streams', True, (0,0,0))
    streamButtonText = boldFont.render('Stream', True, (255,255,255))

    screen.blit(streamText,(20,20))

    xoffs = 450
    yoffs = 20
    pygame.draw.rect(screen,"#023047",[(width/2) + xoffs,yoffs,140,40],border_radius=15)
        
    screen.blit(streamButtonText , ((width/2)+xoffs+13,yoffs-2))

    streamxOffs = 160
    streamBoxIndex = 0
    for streams in availStream:
        pygame.draw.rect(screen,"#023047",[(streamBoxIndex*streamxOffs)+20,100,150,150],border_radius=15)
        screen.blit(boldFont.render(clientName[streamBoxIndex], True, (255,255,255)),((streamBoxIndex*streamxOffs)+30 + len(clientName[streamBoxIndex])/2,150))
        streamBoxIndex += 1

    if(n == 0 and i<5):
            availStream[f'192.168.{i}.10'] = f"G{i}-PC"
            i = i+1
            n = 100
    else:
        n = n-1
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()



# CLIENT

# KB = 1024

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # host_ip = '192.169.51.48'
# host_ip = '192.168.191.48'
# # host_ip = '192.168.216.219'
# # host_ip = socket.gethostbyname(socket.gethostname())
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



# SERVER