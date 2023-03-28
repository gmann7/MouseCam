import sys
import numpy as np
import time
import cv2
import HandTrackingModule as htm
import autopy

wCam = 640
hCam = 480
frameReduction = 100
pTime = 0
detector = htm.handDetector(maxHands=1)
#Connect to Video Capture device (webcam or virtual cam)
cap = cv2.VideoCapture(1)

cap.set(3,wCam)
cap.set(4,hCam)

wScreen, hScreen = autopy.screen.size()
print(wScreen, hScreen)
while True:
    success,img = cap.read()
    #print(success)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    
    #Get fingers info  
    if(len(lmList)!=0):
        x1,y1 = lmList[8][1:] #index finger
        x2,y2 = lmList[12][1:] #middle finger 

    #Check which finger is up
    fingers = detector.fingersUp(lmList)
    print(fingers)
    cv2.rectangle(img,(frameReduction,frameReduction),(wCam-frameReduction, hCam-frameReduction),(255,0,0),2)
    #Check if finger is moving
    if detector.result.multi_hand_landmarks:
        if fingers[1]==1 and fingers[2]==0:
            #convert coordinates into position.
            x3 = np.interp(x1, (frameReduction,wCam-frameReduction),(0,wScreen))
            y3 = np.interp(y1, (frameReduction,hCam-frameReduction),(0,hScreen))
            #Normalize values
            #Move Mouse
            autopy.mouse.move(wScreen-x3,y3)
            cv2.circle(img,(x1,y1),15, (255,0,255),cv2.FILLED);

    #Check if in clicking mode (doing index and middle for now, but should be index and thumb becuase i said so)
    if detector.result.multi_hand_landmarks:
        if fingers[1]==1 and fingers[2]==1:
            length, img, _ = detector.findDistance(8,12,img)
            print(length)
    #Find distance between fingers and click mouse if so

    #Show Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)

    #Show image
    cv2.imshow("Cam", img)
    #Check wheter q has been hit and stops the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows

    
