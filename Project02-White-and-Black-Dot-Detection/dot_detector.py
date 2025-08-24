import cv2 as cv

# path = "BlackDots.jpg" 
path= "WhiteDots.png"

gray = cv.imread(path,0)

#Threshold 
# th,threshed = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU) # For Black Dot Detection
th, threshed = cv.threshold(gray,100,255,cv.THRESH_BINARY|cv.THRESH_OTSU) # For White Dot Detection

#Find Contours
cnts = cv.findContours(threshed,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)[-2]

#Filtering Contours
s1= 3
s2= 20
xcnts=[]

for cnt in cnts:
    if s1 < cv.contourArea(cnt) < s2:
        xcnts.append(cnt)

# print(f"The Total Number Of Black Dots is {len(xcnts)}")        
print(f"The Total Number Of White Dots is {len(xcnts)}")
