# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:42:02 2016

@author: jussi
"""
import numpy as np
import cv2
from time import sleep

class Cv2FaceTracker:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        self.prev_face_pos = (0.5,0.5)

    def track(self, img):        
        
		# Our operations on the frame come here
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
		faces = self.face_cascade.detectMultiScale(gray, 1.3, 4)
			
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			height, width, channels = img.shape
			self.prev_face_pos = ((x+w/2.0)/width, (y+h/2.0)/height)
			#print x,y
			return self.prev_face_pos 
		
		return None, None
        
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    with Cv2FaceTracker(show_result=True) as ft:
        while True:
            print ft.track()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
if __name__ == '__main__':
    main()
