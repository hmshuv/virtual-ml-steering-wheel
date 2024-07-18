import cv2
import imutils
from imutils.video import VideoStream
import numpy as np 
from pynput.keyboard import Key, Controller

keyboard = Controller()

cam = VideoStream(src=0).start()
currentKey = list()

while True:
    key_pressed = False

    img = cam.read()
    img = np.flip(img, axis=1)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(img_hsv, (11, 11), 0)

    colourLower = np.array([])
    colourUpper = np.array([])