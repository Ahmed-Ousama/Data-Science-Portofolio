#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import imutils
import os


# In[3]:


TrDict= {'csrt': cv2.TrackerCSRT_create,
          'kcf': cv2.TrackerKCF_create,
          'boosting': cv2.legacy.TrackerBoosting_create,
          'mil': cv2.TrackerMIL_create,
         'tld': cv2.legacy.TrackerTLD_create,
         'medianflow':cv2.legacy.TrackerMedianFlow_create,
         'mosse': cv2.legacy.TrackerMOSSE_create
        }


# In[5]:


tracker= cv2.legacy.MultiTracker_create()


# In[ ]:


if __name__ == "__main__":
    k=2
    for in range(k):
    # find the webcam
        v = cv2.VideoCapture(0)
        ret , frame = cap.read()
        cv2.imshow('Frame',frame)
        bb= cv2.selectROI('frame', frame)
        tracker_i= TrDict['csrt']()
        trackers.add(tracker_i, frame, bb)        
        cv2.waitKey(0)
        cv2.destroAllWindows()


    # record videof
    while (cap.isOpened()):
        ret, frame= v.read()
        (success, boxes)= tracker.update(frame)
        if sucess :
            for box in boxes:
                (x,y,w,h)= [int(a) for a in box]
                 cv2.rectangle(frame, (x,y), (x+w, y+h), (100,255,0),2)
                
   
        cv2.imshow('Frame', frame)


       
       

        # Tiny Pause
        if cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()     

