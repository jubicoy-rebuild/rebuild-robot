#!/usr/bin/env python
""" This is the controller / server script of the Jubic RE:Build event. Run it and then run the
 script on the robot"""

import socket
import pygame
import os.path
import sys
import cv2

FACE_HOMING_DEVICE = True
HOMING_WIDTH = 0.33 # if face is 33% from the left or right of the screen, turn
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

if FACE_HOMING_DEVICE:
  import facetrack
  facetracker = facetrack.Cv2FaceTracker()

print "Waiting for a client..."
conn, addr = s.accept()
print '... yesss! Connection from address:', addr

valid_img = None
track_left = 0
track_right = 0
enable_tracking = False
face_xr, face_yr = None, None
while True:
  screen.fill((white))
  if os.path.isfile(FILE_TO_PROCESS):
    try:
      face_xr, face_yr = None, None
      img = pygame.image.load(FILE_TO_PROCESS)
      valid_img = img
      if FACE_HOMING_DEVICE and enable_tracking:
        track_img = cv2.imread(FILE_TO_PROCESS)
        face_xr, face_yr = facetracker.track(track_img)
        if face_xr!=None:
          if face_xr > 1.00-HOMING_WIDTH:
            track_left = 1
            track_right = 0
          elif face_xr < HOMING_WIDTH:
            track_right = 1
            track_left = 0
          else:
            track_left = 1
            track_right = 1
        else:
          track_left = 0
          track_right = 0

    except:
      print "Non critical error in reading or processing file:", sys.exc_info()[0]
      
    screen.blit(img,(0,0))
    if face_xr and face_yr:
      pygame.draw.circle(screen, (255,0,0), (int(face_xr*w),int(face_yr*h)), int(w/12), 3)
      pygame.draw.line(screen, (255,0,0), (int(face_xr*w-w/11),int(face_yr*h)), (int(face_xr*w+w/11),int(face_yr*h)), 3)
      pygame.draw.line(screen, (255,0,0), (int(face_xr*w),int(face_yr*h-w/11)), (int(face_xr*w),int(face_yr*h+w/11)), 3)

  aslabel = myfont.render("Press 'a' to drive left track, 's' for right", 1, (255,255,0))
  aslw,aslh = aslabel.get_size()
  screen.blit(aslabel, (w/2-aslw/2, h-h/6))
  if FACE_HOMING_DEVICE:
    if enable_tracking:
      elabel = myfont.render("'e' to trun the face follower OFF", 1, (255,255,0))
    else:
      elabel = myfont.render("'e' to trun the face face follower ON", 1, (255,255,0))
    elw,elh = label.get_size()
    screen.blit(elabel, (w/2-elw/2, h-h/6+elh))

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
      if event.key == ord("e"):
        enable_tracking = not enable_tracking
        track_left = 0
        track_right = 0

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
