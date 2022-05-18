#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2

if __name__ == "__main__":
    # find the webcam
    capture = cv2.VideoCapture(0)

    # video recorder
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoOut = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

    # record video
    while (capture.isOpened()):
        ret, frame1 = capture.read()
        ret, frame2= capture.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
    
        _, thresh = cv2.threshold(blur, 30, 225, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=10)
        contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        #draw = cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        
        for contour in contours :
            (x, y, w, h) = cv2.boundingRect(contour)
        
            if cv2.contourArea(contour) < 400:
                continue
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "Status:  {}".format('movement'), (10,20)
                     ,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0, 255), 3)
        
        image = cv2.resize(frame1, (1280,720))
        #out.write(image)
        #cv2.imshow("motion detection", frame1)
        
        if ret:
            videoOut.write(image)
            cv2.imshow('Video Stream', frame1)
            #cv2.imshow("thresh", thresh)
            cv2.imshow("dilated", dilated)
            #cv2.imshow("draw", draw)

        else:
            break

        # Tiny Pause
        if cv2.waitKey(40) == 27:
            break

    capture.release()
    videoOut.release()
    cv2.destroyAllWindows()


# In[ ]:




