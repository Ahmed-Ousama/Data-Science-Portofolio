#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os


# In[4]:


img= cv2.imread('IMG_20200831_215142_430.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[11]:


sift= cv2.SIFT_create()
kp= sift.detect(gray)
img = cv2.drawKeypoints(gray,kp,img, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


sift= cv2.SIFT_create()
kp, des= sift.detectAndCompute(gray, None)
img = cv2.drawKeypoints(gray,kp,img, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:





# 

# In[ ]:





# In[ ]:





# In[ ]:




