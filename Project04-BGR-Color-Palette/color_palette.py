import cv2 as cv
import numpy as np

def emptyFunction(value):
    pass

image = np.zeros((512,512,3),np.uint8)
WindowName ="BGR Color Palette"

cv.namedWindow(WindowName)

cv.createTrackbar("Blue",WindowName,0,255,emptyFunction)
cv.createTrackbar("Green",WindowName,0,255,emptyFunction)
cv.createTrackbar("Red",WindowName,0,255,emptyFunction)

while(True):
    cv.imshow(WindowName,image)
    if cv.waitKey(1) == 27:
        break
    
    blue = cv.getTrackbarPos("Blue",WindowName)
    green = cv.getTrackbarPos("Green",WindowName)
    red = cv.getTrackbarPos("Red",WindowName)
    
    image[:]=[blue,green,red]
    
    