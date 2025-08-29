import cv2 as cv
import gc
gc.collect()

VideoObj = cv.VideoCapture("Project05-Playing-a-video-in-Reverse-Mode/Video2.mp4")

counter = 0
frame_list=[]

while True :
    check, frame = VideoObj.read()
    if not check :
        break
    frame_list.append(frame)
    
VideoObj.release()

frame_list.reverse()

while counter == 0:
    for frame in frame_list:
        cv.imshow("Reversed Video", frame)
        if cv.waitKey(25) & 0xFF == ord("q"):
            counter =1
            break
    
cv.destroyAllWindows()

    