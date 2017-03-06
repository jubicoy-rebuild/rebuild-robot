
#!/usr/bin/env python

import socket
import drive2

drive2.setup()

TCP_IP = '192.168.0.21'
TCP_PORT = 5005
BUFFER_SIZE = 4
MESSAGE = "rdy"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
  s.send(MESSAGE)
  data = s.recv(BUFFER_SIZE)
  #print "received data:", data
  control = list(data)
  if control[0] == '1':
    if control[1] == '1':
      drive2.forward()
    else:
      drive2.steer_right()
  else:
    if control[1] == '1':
      drive2.steer_left()
    else:
      drive2.stop()
s.close()
