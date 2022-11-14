# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 09:36:20 2022

@author: PLAP033
"""

import cv2 
import winsound
# cam1 = cv2.VideoCapture("rtsp://v6:Wesix@21@192.168.1.18:554/cam/realmonitor?channel=2&subtype=0")
cam1 = cv2.VideoCapture(0)
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
# out = cv2.VideoWriter('security_cam_demo_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10.0, (960,1080))
def detect_motion(cam):
    _,frame1 = cam.read()
    _,frame2 = cam.read()
    # print(frame1.shape)
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0,255,133))
    for cnt in contours:
        if cv2.contourArea(cnt) < 4500:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,0,255),3)
        winsound.Beep(400, 150)
    return frame1
while True:
    cam1_output = detect_motion(cam1)
    cv2.imshow("cam1", cam1_output)
    # out.write(cam1_output)
    key = cv2.waitKey(1)
    if key == 27:
        break
# out.release()
cam1.release()
cv2.destroyAllWindows()