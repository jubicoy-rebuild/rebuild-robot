#######################################################################
# THIS IS A DIRTY EXAMPLE, DO NOT TAKE SERIOUSLY                      #
#######################################################################


import CHIP_IO.GPIO as GPIO
#import CHIP_IO.PWM as PWM
#import CHIP_IO.SOFTPWM as SPWM

import time

duty = 100
freq = 100

def setup():
	GPIO.setup("CSID0", GPIO.OUT)
	GPIO.setup("CSID1", GPIO.OUT)
	GPIO.setup("CSID2", GPIO.OUT)
	GPIO.setup("CSID3", GPIO.OUT)

m1_1 = "CSID0"
m1_2 = "CSID1"
m2_1 = "CSID2"
m2_2 = "CSID3"


def forward():
        GPIO.output(m1_1, GPIO.HIGH)
        GPIO.output(m1_2, GPIO.LOW)
        GPIO.output(m2_1, GPIO.HIGH)
        GPIO.output(m2_2, GPIO.LOW)

def reverse():
        GPIO.output(m1_1, GPIO.LOW)
        GPIO.output(m1_2, GPIO.HIGH)
        GPIO.output(m2_1, GPIO.LOW)
        GPIO.output(m2_2, GPIO.HIGH)

def steer_right():
        GPIO.output(m1_1, GPIO.LOW)
        GPIO.output(m1_2, GPIO.HIGH)
        GPIO.output(m2_1, GPIO.HIGH)
        GPIO.output(m2_2, GPIO.LOW)

def steer_left():
        GPIO.output(m1_1, GPIO.HIGH)
        GPIO.output(m1_2, GPIO.LOW)
        GPIO.output(m2_1, GPIO.LOW)
        GPIO.output(m2_2, GPIO.HIGH)

def stop():
        GPIO.output(m1_1, GPIO.LOW)
        GPIO.output(m1_2, GPIO.LOW)
        GPIO.output(m2_1, GPIO.LOW)
        GPIO.output(m2_2, GPIO.LOW)

def main():
	GPIO.setup("CSID0", GPIO.OUT)
	GPIO.setup("CSID1", GPIO.OUT)
	GPIO.setup("CSID2", GPIO.OUT)
	GPIO.setup("CSID3", GPIO.OUT)
	
	cmd = ""
	while cmd!="q":
  		cmd = raw_input("q,wasd,x? :")
  		if cmd=="w":
			forward()
  		if cmd=="a":
			steer_left()
		if cmd=="d":
			steer_right()
		if cmd=="s":
    			reverse()
		if cmd=="x":
			stop()
	stop()
	GPIO.cleanup()
                                                                                                                                                        