#importing modules
import time
import math
import cv2   
import numpy as np
import serial
ser1=serial.Serial('COM3',9600);

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
    ret ,img = cap.read()
    #converting frame(img i.e BGR) to HSV (hue-saturation-value)
    hsv = cv2.cvtColor( img,cv2.COLOR_BGR2HSV)

    #definig the range of red color
    red_lower=np.array([136,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    #defining the Range of Blue color
    
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
    #defining the Range of green color
    
    green_lower = np.array([40,108,113],np.uint8)
    green_upper = np.array([94,255,255],np.uint8)
    
    #defining the Range of yellow color
        
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)

    #defining the Range of brown color
        
    brown_lower=np.array([0,38,51],np.uint8)
    brown_upper=np.array([24,153,102],np.uint8)

    #finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    green=cv2.inRange(hsv,green_lower,green_upper)
    brown=cv2.inRange(hsv,brown_lower,brown_upper)
    
    #Morphological transformation, Dilation     
    kernal = np.ones((5 ,5), "uint8")
    red=cv2.dilate(red, kernal)

    res=cv2.bitwise_and(img, img, mask = red)

    blue=cv2.dilate(blue,kernal)
    
    res1=cv2.bitwise_and(img, img, mask = blue)


    yellow=cv2.dilate(yellow,kernal)
    
    res2=cv2.bitwise_and(img, img, mask = yellow)

    green=cv2.dilate(green, kernal)

    res3=cv2.bitwise_and(img, img, mask = green)

    brown=cv2.dilate(brown, kernal)

    res4=cv2.bitwise_and(img, img, mask = brown)


    #Tracking the Red Color

    contours,_=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
            for i in range(8):
                ser1.write('aaaaaaaa'.encode())
            
            
        else:
            for i in range(8):
                ser1.write('bbbbbbbb'.encode())
            
            
    #Tracking the Blue Color
    contours,_=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            for i in range(8):
                ser1.write('cccccccc'.encode())
            
        else:
            for i in range(8):
                ser1.write('dddddddd'.encode())
            
    #Tracking the yellow Color
    contours,_=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
            for i in range(8):
                ser1.write('eeeeeeee'.encode())
        else:
            for i in range(8):
                ser1.write('ffffffff'.encode())

    #Tracking the green Color
    contours,_=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
            for i in range(8):
                ser1.write('gggggggg'.encode())
        else:
            for i in range(8):
                ser1.write('hhhhhhhh'.encode())
    #Tracking the brown colour
    contours,_=cv2.findContours(brown,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"brown  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
            for i in range(8):
                ser1.write('iiiiiiii'.encode())
        else:
            for i in range(8):
                ser1.write('jjjjjjjj'.encode())
            
        
    cv2.imshow("Color Tracking",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break  
          
