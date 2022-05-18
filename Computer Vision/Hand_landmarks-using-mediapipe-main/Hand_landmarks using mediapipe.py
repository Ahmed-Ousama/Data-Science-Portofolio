#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import mediapipe as mp
import os 


# In[13]:



mphands = mp.solutions.hands
hands= mphands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime= 0
cTime= 0

if __name__ == "__main__":
    # find the webcam
    capture = cv2.VideoCapture(0)
 
    while (capture.isOpened()):
        _, img = capture.read()
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img)
        #print(results.multi_hand_landmarks)

            

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for idd, lm in enumerate(handLms.landmark):#enumerate return index and value
                    print(idd, lm)
                    h , w, c = img.shape #c refers to chanels
                    cx, cy, = int(lm.x*w), int(lm.y*h)
                    print(idd, cx, cy)
                    if idd == 0:
                        cv2.circle(img,(cx,cy),9 , (255,0,255), cv2.FILLED)
                        
                mpDraw.draw_landmarks(img ,handLms,
                                         mphands.HAND_CONNECTIONS)
        cv2.imshow('Hand Landmarks', img)
       
       

        # Tiny Pause
        if cv2.waitKey(40) == 27:
            break

    capture.release()
    cv2.destroyAllWindows()        


# In[ ]:




