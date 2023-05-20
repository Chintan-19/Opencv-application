# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:01:30 2023

@author: Lenovo
"""



import cv2 
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
zoom_level=1.0
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
         
        frame_height, frame_width, _ = frame.shape
        frame = cv2.resize(frame, None, fx=zoom_level, fy=zoom_level)
 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        
        
       

  
        key = cv2.waitKey(1)
 
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("capturing snapshot...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 100x100 scale...")
            img_ = cv2.resize(gray,(100,100))
            print("Snapshot captured")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            
  

    # Zoom in and out based on key press
        if key == ord('+'):  # Zoom in
            zoom_level += 0.1
        elif key == ord('-'):  # Zoom out
            zoom_level -= 0.1

        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break