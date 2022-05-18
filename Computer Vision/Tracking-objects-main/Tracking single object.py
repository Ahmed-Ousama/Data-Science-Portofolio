#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import imutils
import os


# In[6]:


TrDict= {'csrt': cv2.TrackerCSRT_create,
          'kcf': cv2.TrackerKCF_create,
          'boosting': cv2.legacy.TrackerBoosting_create,
          'mil': cv2.TrackerMIL_create,
         'tld': cv2.legacy.TrackerTLD_create,
         'medianflow':cv2.legacy.TrackerMedianFlow_create,
         'mosse': cv2.legacy.TrackerMOSSE_create
        }


# In[7]:


tracker = TrDict['csrt']() #() to bring all functions in csrt
tracker= cv2.TrackerCSRT_create()


# In[8]:


if __name__ == "__main__":
    # find the webcam
    v = cv2.VideoCapture(0)
    ret , frame = cap.read()
    frame= imutils.resize(frame, width=600)
    bb= cv2.selectROI('frame', frame)
    tracker.init(frame, bb)
    #first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    #first_gray = cv2.GaussianBlur(first_gray, (5,5), 0)
    # video recorder


    # record videof
    while (cap.isOpened()):
        ret, frame= v.read()
        frame= imutiils.resize(frame, width= 600)
        (success, box)= tracker.update(frame)
        if sucess :
            (x,y,w,h)= [int(a) for a in box]
             cv2.rectangle(frame, (x,y), (x+w, y+h), (100,255,0),2)
                
   
        cv2.imshow('Frame', frame)
        #cv2.imshow('frame ', frame)
        #cv2.imshow('difference', difference)
        prev= new
        _, new = cap.read()
        new = cv2.flip(new, 1)

       
       

        # Tiny Pause
        if cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()     


# In[ ]:




