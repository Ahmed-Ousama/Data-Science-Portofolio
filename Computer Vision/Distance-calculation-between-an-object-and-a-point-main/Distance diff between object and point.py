#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[7]:


if __name__ == "__main__":
    # find the webcam
    cap = cv2.VideoCapture(0)
    ret , prev = cap.read()
    ret , new = cap.read()    
    #first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    #first_gray = cv2.GaussianBlur(first_gray, (5,5), 0)
    # video recorder


    # record videof
    while (cap.isOpened()):
        diff = cv2.absdiff(prev , new )
        #speed-up the processing
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        #noise eliimination
        diff = cv2.blur(diff, (5,5))
        _, thresh = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None)
        thresh = cv2.erode(thresh, np.ones((4,4)),1)
        contor,_= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #point 
        cv2.circle(prev, (20,200), 5, (0,0,255), -1)#filling
        for contors in contor:
            if cv2.contourArea(contors) > 20000 :
                #coordinates
                (x,y,w,h)= cv2.boundingRect(contors)
                #center circle inside contour
                (x1,y1), rad= cv2.minEnclosingCircle(contors)
                x1= int(x1)
                y1= int(y1)
                #connecting line
                cv2.line(prev, (20,200),(x1,y1), (255,0,0), 4)
                cv2.putText(prev, "{}".format(int(np.sqrt((x1- 20)**2 + (y1-200)**2))), (100,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0, 255), 3)
                cv2.rectangle(prev, (x,y), (x+w, y+h), (0,255,0),2)
                cv2.circle(prev, (x1,y1), 5, (0,0,255), -1)

   
        cv2.imshow('ORIG', prev)
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




