import cv2 as cv

def ExtractFrames(path, Interval, Duration) :

    VideoObj =cv.VideoCapture(path)   #Storing the video in variable VideoObj
    FPS = int(VideoObj.get(cv.CAP_PROP_FPS)) # Counting Frames Per Second(FPS)
    print(FPS)
    FrameInterval = int(FPS * Interval)
    

    count = 1
    saved = 1
    success = 1

    while success :
        success, frame = VideoObj.read()

        if count > FPS * Duration:
            break

        if count % FrameInterval == 0:
            cv.imwrite("Frame%d.jpg" % saved,frame)
            saved+=1

        count+=1

    VideoObj.release()

    print(f"Saved {saved - 1} frames")

if __name__== '__main__':

    path = input("Enter video path: ")
    Interval = float(input("Enter interval (in seconds between frames to save): "))
    Duration = int(input("Enter duration (in seconds to process video): "))

    ExtractFrames(path,Interval,Duration)






    
