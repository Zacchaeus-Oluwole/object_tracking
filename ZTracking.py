import cv2

video = cv2.VideoCapture(0)

#This tracker is fast but low high accuracy
tracker = cv2.TrackerMOSSE_create()

#This tracker is accurate but is slow
#tracker = cv2.TrackerCSRT_create()

# craete ROI tracking box
check, capture = video.read()
box = cv2.selectROI("Select a ROI and then press SPACE or ENTER button!", capture, False)
tracker.init(capture,box)

def drawBox(capture, box):
    x,y,w,h = int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(capture, (x,y), ((x+w),(y+h)), (255,0,255),3,1)
    cv2.putText(capture, "Tracking",(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

# put your main code in the while loop, to run repeatedly:
while True:

    timer = cv2.getTickCount()
    check, capture = video.read()
    check, box = tracker.update(capture)

    # If check is True, draw box
    if check:
        drawBox(capture, box)
    else:
        cv2.putText(capture, "Lost",(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(capture, str(int (fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

    cv2.imshow("ZTracking", capture)
    cv2.waitKey(1)
