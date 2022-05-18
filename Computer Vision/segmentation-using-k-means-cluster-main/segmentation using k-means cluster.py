#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import cv2 
import os 
import matplotlib.pyplot as plt


# In[3]:


os.chdir("desktop")


# In[5]:


img = cv2.imread('IMG-20170401-WA0069.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[6]:


#from 3d to 2d of RGB values
pixel_values = img.reshape((-1,3))
#to float 32
pixel_values = np.float32(pixel_values)


# In[7]:


print(pixel_values.shape)


# In[14]:


criteria= (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.95)
k= 5
_, labels, (centers)= cv2.kmeans(pixel_values, k,None, criteria, 10 , cv2.KMEANS_RANDOM_CENTERS)


# In[15]:


#convert back to unit8
centers= np.uint8(centers)
#flatten
labels= labels.flatten()
#pixel> centroid color
segmented_image = centers[labels.flatten()]
#reshape > org.img
segmented_image = segmented_image.reshape(img.shape)
#show the image
plt.imshow(segmented_image)
plt.show


# In[22]:


#DISABLING A CLUSTER 
masked_img= np.copy(img)
#reshaping
masked_img = masked_img.reshape((-1,3))
#cluster no
cluster= 2
masked_img[labels== cluster]= [0,0,0]
#reshape
masked_img= masked_img.reshape(img.shape)
#img
plt.imshow(segmented_image)
plt.imshow(masked_img)
plt.show()


# In[ ]:




