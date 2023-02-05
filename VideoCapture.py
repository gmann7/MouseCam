import sys
import numpy as np
import time
import cv2
import HandTrackingModule as htm

widhtCam = 640
heightCam = 480
pTime = 0
detector = htm.handDetector(maxHands=1)
#Connect to Video Capture device (webcam or virtual cam)
cap = cv2.VideoCapture(1)

cap.set(3,widhtCam)
cap.set(4,heightCam)

while True:
    success,img = cap.read()
    #print(success)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)

    #Get fingers info  
    if(len(lmlist)!=0):
        x1,y1 = lmlist[8][1:] #index finger
        x2,y2 = lmlist[12][1:] #middle finger

        print(x1,y1,x2,y2)  

    #Check which finger is up
    
    #Check if finger is moving
        #convert coordinates into p sition.

    #Normalize values

    #Move Mouse

    #Check if in clicking mode
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

    
