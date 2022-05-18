
 
import cv2 
import numpy as np 
from imutils.object_detection import non_max_suppression
 
filename = 'pedestrians_on_street_1.mp4'
file_size = (1920,1080) 
scale_ratio = 1 
 
output_filename = 'pedestrians_on_street.mp4'
output_frames_per_second = 20.0
 
def main():
 
  hog = cv2.HOGDescriptor()
     
  hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
     
  cap = cv2.VideoCapture(filename)
 
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  result = cv2.VideoWriter(output_filename,  
                           fourcc, 
                           output_frames_per_second, 
                           file_size) 
     
  while cap.isOpened():
         
    success, frame = cap.read() 
         
    if success:
         
      width = int(frame.shape[1] * scale_ratio)
      height = int(frame.shape[0] * scale_ratio)
      frame = cv2.resize(frame, (width, height))
             
      orig_frame = frame.copy()
             
      (bounding_boxes, weights) = hog.detectMultiScale(frame, 
                                                       winStride=(16, 16),
                                                       padding=(4, 4), 
                                                       scale=1.05)
 
      for (x, y, w, h) in bounding_boxes: 
            cv2.rectangle(orig_frame, 
            (x, y),  
            (x + w, y + h),  
            (0, 0, 255), 
             2)
                         

      bounding_boxes = np.array([[x, y, x + w, y + h] for (
                                x, y, w, h) in bounding_boxes])
             
      selection = non_max_suppression(bounding_boxes, 
                                      probs=None, 
                                      overlapThresh=0.45)
         
      # draw the final bounding boxes
      for (x1, y1, x2, y2) in selection:
        cv2.rectangle(frame, 
                     (x1, y1), 
                     (x2, y2), 
                     (0, 255, 0), 
                      4)
         
      result.write(frame)
             
      cv2.imshow("Frame", frame)    
 
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
         
    else:
      break
             
  # Stop when the video is finished
  cap.release()
     
  # Release the video recording
  result.release()
     
  # Close all windows
  cv2.destroyAllWindows() 
 
main()