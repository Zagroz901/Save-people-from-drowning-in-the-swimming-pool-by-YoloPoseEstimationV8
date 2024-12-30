from ultralytics import YOLO
import cv2
import numpy as np
from tracker import *
from mutagen.mp3 import MP3
import time
import miniaudio
def calc_angle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180/np.pi)
    if angle > 180.0:
        angle = 360-angle
    return angle

frame_check = 7
flag = 0
file='audio\\assets_alarm.mp3'
audio = MP3(file)
length=audio.info.length
tracker=Tracker()
model = YOLO(r"Weights\yolov8n-pose.pt")
cap= cv2.VideoCapture("Video\\vid.mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter(
    'output_video.avi',  
    cv2.VideoWriter_fourcc(*'XVID'),  
    fps,  
    (frame_width, frame_height)
)

while True:
    ret,frame = cap.read()
    if ret ==  False:
        break
    h , w , c = frame.shape
    results= model.predict(frame,classes=[0])
    boxes = results[0].boxes
    result_of_keypoints= results[0].keypoints.xy
    points=[]
    for box in boxes:
        x1,y1,x2,y2=map(int,box.xyxy.flatten())
        points.append([x1,y1,x2,y2])
    boxes_id = tracker.update(points)
    num=len(points)
    id= []
    for box_id in boxes_id:
        x , y , w , h , idd = box_id
        id.append(idd)    
        cv2.rectangle(frame,(x,y),(w,h),(0,255,0),2)
        cv2.putText(frame,'number of persons is='+str(num),(20,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),3)
        cv2.putText(frame,'person ID is='+str(idd),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
             
    for keypoints in result_of_keypoints:
        left_shoulder = keypoints[5]
        right_shoulder = keypoints[6]
        left_elbow = keypoints[7]
        right_elbow = keypoints[8]
        left_wrist = keypoints[9]
        right_wrist = keypoints[10]
        l_ang = calc_angle(left_shoulder,left_elbow,left_wrist)
        r_ang = calc_angle(right_shoulder,right_elbow,right_wrist)
        # cv2.putText(frame,str(int(l_ang)),np.multiply(left_elbow.type(torch.int),[640,480]),
        #             cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
        # cv2.putText(frame,str(int(r_ang)),tuple( np.multiply(right_elbow.type(torch.int),[640,480])),
        #             cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
        if left_wrist[1]*h < left_elbow[1]*h < left_shoulder[1]*h and l_ang > 150:
            flag += 1
            if flag >= frame_check:
                cv2.putText(frame,'Warnning!!! someone need help',(20,75),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                stream = miniaudio.stream_file(file)
                with miniaudio.PlaybackDevice() as device:
                    device.start(stream)
                    time.sleep(length)
            
        elif right_wrist[1]*h < right_elbow[1]*h < right_shoulder[1]*h and r_ang > 150:
    
            flag += 1
            if flag >= frame_check:
                cv2.putText(frame,'Warnning!!! someone need help',(20,75),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                stream = miniaudio.stream_file(file)
                with miniaudio.PlaybackDevice() as device:
                    device.start(stream)
                    time.sleep(length)
    out.write(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break
out.release()
cap.release()
cv2.destroyAllWindows()

