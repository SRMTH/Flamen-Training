import numpy as np
import cv2 as cv

def get(now):
    cap=cv.VideoCapture(1)
    ex=0
    why=0
    test=(0,0)

    u=116
    v=87

    while True:

        _, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
        mask = cv.inRange(hsv, np.array([0,u-30,v-30]),np.array([255,u+30,v+30]))
        im3, contours1, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        cv.drawContours(frame, contours1, -1 , (0,0,255), 3)

        cnt = sorted(contours1, key=cv.contourArea)

        (m,n),radius = cv.minEnclosingCircle(cnt[0])
        center = (int(m),int(n))
        r = int(radius)

        if test!=center:
                cv.circle(frame,center,int(radius),(0,255,0),2)
                
        test=center
        cv.imshow("im3",frame)
        if now:
                return [center[0],center[1]]
        if cv.waitKey(5)==ord('c'):
                break