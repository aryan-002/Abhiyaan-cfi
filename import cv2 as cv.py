import cv2 as cv
from cv2 import VideoCapture
import numpy as np
VideoCapture=cv.VideoCapture(2)
while true:
    ret,frame = VideoCapture.read90
    if not ret;break

    grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2FRAY)
    blueFrame=cv.GaussianBlur(grayFrame,(17,17),0)

    cv.imshow('blurFrame',blur)



    cv.imshow("frame",frame)
    if cv.waitkey(1) & 0xFF ==ord('q'): break
VideoCapture.release()
cv.destroyAllWindows