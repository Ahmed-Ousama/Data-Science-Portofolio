# Movement-Detection
This repository explains how to detect movement in a video or live-feed video and draw a rectangle around it using the OpenCV library from python

## The idea behind detection:
Using OpenCV library we detect the change between frames captured by the camera so while the feed is true the code will detect any differences between frames and then choosing the area of the thing that is moving, we define the person area here as a target, then we draw a rectangle around the moving person.

## Preprocessing video:
1- We convert the video to the gray scale.

2- The Gaussian Blur help  solving the problem of lighthing condition that will exist in the video.

3- The treshold command will isolate the moving objects in white and black scene, white as a moving object, and will remove the other objects exisit within the frame 

4- The dilation will solve the problem of empty contours and noises existance and will help to detect the whole area of moving object.




