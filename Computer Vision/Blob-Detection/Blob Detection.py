#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as lb
import cv2


# In[3]:


image= cv2.imread("#Image Name")


# In[6]:


params = cv2.SimpleBlobDetector_Params()


# In[8]:


#Parameters Tuning
#Treshold
params.minThreshold= 0
params.maxThreshold= 255
#Area 
params.filterByArea= True
params.minArea= 50
params.maxArea= 10000
#Color
params.filterByColor= False
params.blobColor= 0 #black
#Circularity
params.filterByCircularity= True
params.minCircularity= 0.5
params.maxCircularity= 1
#Convexity
params.filterByConvexity= True
params.minConvexity= 0.1
params.maxConvexity= 1


# In[9]:


detector = cv2.SimpleBlobDetector_create(params)
keypoints= detector.detect(image)


# In[10]:


print ("#No.Blobs detected are", len(keypoints))


# In[ ]:


img_with_blobs = cv2.drawKeypoints(image, keypoints,None,(0,0,255), cv2.Draw_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)#Cricle around blobs with red color)
plt.imshow("Keypoints", img_with_blobs)
cv2.waitkey(0)
cv2.destroyAllWindows()
                                   
    

