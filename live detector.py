import cv2
from numpy import empty
def empty(img):
    pass

vid =cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",600,900)
cv2.createTrackbar("hue_min","Trackbar",0,179,empty)
cv2.createTrackbar("hue_max","Trackbar",0,179,empty)
cv2.createTrackbar("sat_min","Trackbar",0,255,empty)
cv2.createTrackbar("sat_max","Trackbar",255,255,empty)
cv2.createTrackbar("val_max","Trackbar",0,255,empty)
cv2.createTrackbar("val_min","Trackbar",255,255,empty)
while True:
    ret,img =vid.read()

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hue_min = cv2.getTrackbarPos("hue_min","Trackbar")
hue_max = cv2.getTrackbarPos("hue_max","Trackbar")
sat_min = cv2.getTrackbarPos("hue_min","Trackbar")
sat_max = cv2.getTrackbarPos("hue_max","Trackbar")
val_min = cv2.getTrackbarPos("hue_min","Trackbar")
val_max = cv2.getTrackbarPos("hue_max","Trackbar")
lower=np.array([hue_min,sat_min,val_min])
upper=np.array([hue_max,sat_max,val_max])
mask = cv2.inRange(hsv,lower,upper)
cnts.hei=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for c in cnts:
    area=cv2.contourArea(c)
    if area>300:
        peri=cv2.arcLength(c,True)
        approx=cv2.approxPolyDP(c,0.02*peri,True)
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(img,"Points:" +str(len(approx)),(x+w+20, y+h+20), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,2))
        if len(approx)==3:
            cv2.putText(img, "cones" +str(len(approx)),(x+w+20, y+h+20), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,2))
    else:

            cv2.putText(img,"potholes" +str(len(approx)),(x+w+20, y+h+20), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,2))
height, width, _ = frame.shape

cv2.imshow("Frame",img)
cv2.imshow("hsv",hsv)
cv2.mask("Mask",mask)

cv2.putText(frame,colour,(10,50),0,1,(255,0,0),2)
cv2.circle(frame,(cx,cy),5,(255,0,0),3)

cv2.imshow("Frame",frame)
key = cv2.waitKey(1)
if key == 27:
    breakpoint()
    cap.release()
    cv2.destroyAllWondow()