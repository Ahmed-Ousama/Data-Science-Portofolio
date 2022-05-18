import cv2
import os

filename= "The image"

def main():
    #HOGDescriptor 
    hog= cv2.HOGDescriptor()
    #People detector
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    #Loading the image
    img= cv2.imread(filename)
    
    (bounding_boxes, weights)= hog.detectMultiScale( img,
                                                    winStride= (4,4),
                                                    padding= (8,8),
                                                    scale= 1.02)
    
    for (x,y,w,h) in bounding_boxes:
        cv2.rectangle(img, (x,y) , ( x+w, y+h ), (0,0,255), 2)
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
    
main()    