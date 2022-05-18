import cv2
import matplotlib.pyplot as plt
import os 
#_______________________________#

img1= cv2.imread('first image')
img2= cv2.imread('Second image')

orb= cv2.ORB_create()

kp1,des1= orb.detectAndCompute(img1,None)
kp2,des2= orb.detectAndCompute(img2,None)
img= cv2.drawKeypoints(img2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


#Matching algorithm
bf= cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)
matches= bf.match(des1, des2)
matches= sorted(matches, key= lambda x:x.distance)
 
img3= cv2.drawMatches(img1, kp1, img2,kp2, matches[:20],None, flags=2)
cv2.imshow('Keypoints', img3)

plt.imshow(img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
