#!/usr/bin/env python
""" This is the controller / server script of the Jubic RE:Build event. Run it and then run the 
 script on the robot""" 

import socket
import pygame
import os.path
import sys

FILE_TO_PROCESS = '/home/chip/process_me.jpg'
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 4  # Normally 1024, but we want fast response

# Init pygame screen for screen 
white = (255, 64, 64)
w = 640
h = 480
pygame.init()
screen = pygame.display.set_mode((w, h))
screen.fill((white))
myfont = pygame.font.SysFont(None, 20)
label = myfont.render("Waiting for a client...", 1, (255,255,0))
lw,lh = label.get_size()
screen.blit(label, (w/2-lw/2, h/2-lh/2))
pygame.display.flip()

# open socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print "Waiting for a client..."
conn, addr = s.accept()
print '... yesss! Connection from address:', addr

valid_img = None 
track_left = 0
track_right = 0
while True:
  screen.fill((white))
  if os.path.isfile(FILE_TO_PROCESS):
    try:
      img = pygame.image.load(FILE_TO_PROCESS)
      valid_img = img
    except:
	  pass
    screen.blit(img,(0,0))
    
  label = myfont.render("Press 'a' to drive left track, 's' for right", 1, (255,255,0))
  lw,lh = label.get_size()
  screen.blit(label, (w/2-lw/2, h-h/6-lh/2))

  pygame.display.flip()
  pygame.time.delay(100)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT or \
      (event.type == pygame.KEYDOWN and event.key == ord ( "q" )):
      conn.close()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == ord("a"):
        track_left = 1
      if event.key == ord("s"):
        track_right = 1
    elif event.type == pygame.KEYUP:
      if event.key == ord("a"):
        track_left = 0
      if event.key == ord("s"):
        track_right = 0
        
  data = conn.recv(BUFFER_SIZE)
  if data:
    print "received data:", data
    conn.send("%d%d0" % (track_left, track_right))

conn.close()
