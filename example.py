#######################################################################
# THIS IS A DIRTY EXAMPLE, DO NOT TAKE SERIOUSLY                      #
#######################################################################


import CHIP_IO.GPIO as GPIO
import CHIP_IO.PWM as PWM
import CHIP_IO.SOFTPWM as SPWM

#import pygame

import time

from turtle import *

duty = 100
freq = 100

toggle = False

def fwd():
        SPWM.start("CSID0", 50)
        SPWM.set_duty_cycle("CSID0", duty)
        SPWM.set_frequency("CSID0", freq)

        SPWM.start("CSID1", 50)
        SPWM.set_duty_cycle("CSID1", 0)
        SPWM.set_frequency("CSID1", freq)

        SPWM.start("CSID2", 50)
        SPWM.set_duty_cycle("CSID2", duty)
        SPWM.set_frequency("CSID2", freq)

        SPWM.start("CSID3", 50)
        SPWM.set_duty_cycle("CSID3", 0)
        SPWM.set_frequency("CSID3", freq)

def reverse():
        SPWM.start("CSID0", 50)
        SPWM.set_duty_cycle("CSID0", 0)
        SPWM.set_frequency("CSID0", freq)

        SPWM.start("CSID1", 50)
        SPWM.set_duty_cycle("CSID1", duty)
        SPWM.set_frequency("CSID1", freq)

        SPWM.start("CSID2", 50)
        SPWM.set_duty_cycle("CSID2", 0)
        SPWM.set_frequency("CSID2", freq)

        SPWM.start("CSID3", 50)
        SPWM.set_duty_cycle("CSID3", duty)
        SPWM.set_frequency("CSID3", freq)

def steer_left():
        SPWM.start("CSID0", 50)
        SPWM.set_duty_cycle("CSID0", 0)
        SPWM.set_frequency("CSID0", freq)

        SPWM.start("CSID1", 50)
        SPWM.set_duty_cycle("CSID1", duty * 0.75)
        SPWM.set_frequency("CSID1", freq)

        SPWM.start("CSID2", 50)
        SPWM.set_duty_cycle("CSID2", 0)
        SPWM.set_frequency("CSID2", freq)

        SPWM.start("CSID3", 50)
        SPWM.set_duty_cycle("CSID3", duty)
        SPWM.set_frequency("CSID3", freq)


def stop():
	SPWM.cleanup()
	toggle = False


# PUT YOUR CODE HERE
setup(800,600)
home()
pen_size = 2
color("red")
title("Colouring Book")
speed("fastest") # Doesn't make any difference to accuracy, just makes turtle turn animation faster.
drawdist=10 # Distance in pixels pen travels when arrow key is pressed

penup()
###################BUTTON INSTRUCTIONS########################
def move_up():
	global toggle
	if toggle == False:
		fwd()
		toggle = True

def move_down():
	global toggle
	if toggle == False:
		reverse()
		toggle = True

def move_left():
	global toggle
	if toggle == False:
		steer_left()
		toggle = True

def move_right():
	global toggle
	if toggle == False:
		steer_right()
		toggle = True

def space_bar():
	global toggle
	if toggle == False:
		stop()
		toggle = True

################BUTTON TRIGGERS##################
s= getscreen()

s.onkeypress(move_up,"Up")
s.onkey(stop,"Up")
s.onkeypress(move_down,"Down")
s.onkey(stop,"Down")
s.onkeypress(move_left,"Left")
s.onkey(stop,"Left")
s.onkeypress(move_right,"Right")
s.onkey(stop,"Right")
s.onkey(space_bar,"space")

listen()

done()
