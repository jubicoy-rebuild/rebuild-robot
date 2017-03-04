#!/usr/bin/env python
""" This script just shows the feed from the robot inside a Pygame window.
the robot pictureloop.sh script uploads the FILE_TO_PROCESS image to a
ftp server running on this PC, which is then displayed.
"""

import pygame
import os.path

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))

FILE_TO_PROCESS = '/home/chip/process_me.jpg'

valid_img = None 
while True:
  screen.fill((white))
  if os.path.isfile(FILE_TO_PROCESS):
    try:
      img = pygame.image.load(FILE_TO_PROCESS)
      valid_img = img
    except:
	  pass
    screen.blit(img,(0,0))
  pygame.display.flip()
  pygame.time.delay(100)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT or \
      (event.type == pygame.KEYDOWN and event.key == ord ( "q" )):
      sys.exit()

