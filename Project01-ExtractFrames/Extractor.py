import cv2 as cv

def ExtractFrames(path) :

    VideoObj =cv.VideoCapture(path)   #Storing the video in variable cap

    count = 1
    saved = 0
    success = 1

    while success :
        success, frame = VideoObj.read()

        cv.imwrite("Frame%d.jpg" % count,frame)

        count+=1

    VideoObj.release()



if __name__== '__main__':
    ExtractFrames("Video1.mp4")





    
