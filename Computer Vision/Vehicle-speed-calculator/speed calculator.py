#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[13]:


import cv2
import time
import os


# In[7]:


cascade_scr = 'cars.xml'
video_src = 'Relaxing highway traffic.mp4'
fontface = cv2.FONT_HERSHEY_SIMPLEX


# In[8]:


#line a
ax1= 70
ay= 90
ax2= 230


# In[9]:


#line b 
bx1= 15 
by= 25
bx2= 225


# In[10]:


line_dist= 10


# In[11]:


def speed_cal(time):
    try:
        speed = (line_dist/1000)/(time/3600)
        return speed
    except ZeroDivisionError:
        print ("Zero division Error ")


# In[14]:


i=1 
start_time = time.time()


# In[16]:


cap= cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_scr)


# In[32]:


cap= cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_scr)
    
while (cap.isOpened()):
    ret, img = cap.read()
    if (type(img)== type(None)):
        break
    #Bluring to have exacter detection 
    blurred= cv2.blur(img, ksize=(15,15))
    gray= cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    cars= car_cascade.detectMultiScale(gray, 1.1, 2)
    
    #line a #i 
    cv2.line(img, (ax1,ay),(ax2,ay),(255,0,0),2)
    #line b
    cv2.line(img,(bx1,by),(bx2,by),(255,0,0),2)
    
    for (x,y,w,h) in cars :
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)
        cv2.circle(img, (int((x+x+w)/2), int((y+y+h)/2)),5,(0,255,0),-1)
        
        while int(ay) == int((y+y+h)/2):
            start_time = time.time()
            break
                   
        while int(ay) <= int((y+ y+h)/2):
            if int(by) <= int((y+y+h)/2) & int (by+10) >= int((y+y+h)/2):
                cv2.line(img, (bx1, by), (bx2,by), (0,255,0),2)
                speed= speed_Cal(time.time()- start_time)
                print( "car Number"+ str(i) +"Speed: "+str(speed)+ " KM/H")
                i = i+1
                break
            else:
                cv2.putText(img, "Claculating ", (100, 200), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
                
    cv2.imshow('video',img)          
    
    if cv2.waitkey(33)== 27:
        break


# In[ ]:




