import cv2 as cv
import argparse

ref_point = []

def shape_selection(event,x,y,flags,param):
    
    global ref_point
    
    if event == cv.EVENT_LBUTTONDOWN:
        ref_point = [(x,y)]
        
    elif event == cv.EVENT_LBUTTONUP:
        ref_point.append((x,y))
        
        cv.rectangle(image,ref_point[0],ref_point[1],(0,0,0),2)
        cv.imshow("image", image)
        
ap = argparse.ArgumentParser()
ap.add_argument('--i','--image',required=True, help="Path To Image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
clone = image.copy()
cv.namedWindow("image")
cv.setMouseCallback("image", shape_selection)

while True:
    cv.imshow("image", image)
    key = cv.waitKey(1) & 0xFF
    
    if key == ord("r"):
        image = clone.copy()
    
    if key == ord("c"):
        break

if len(ref_point) == 2:
    crop_image= clone[ref_point[0][1]:ref_point[1][1],ref_point[0][0]:ref_point[1][0]]
    cv.imshow("Cropped Image", crop_image)
    cv.waitKey(0)
    
cv.destroyAllWindows()
    
    