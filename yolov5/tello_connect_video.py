import djitello
import sys,os
import time


def connect(IP):
    if IP!="":
        drone=tello.connect(IP)
    else:
        drone=tello.connect()
    return drone

def start_rec(drone,path):
    drone.streamoff()
    drone.streamon()
    frame_read=drone.get_frame_read()
    while 1:
        os.remove(path+'/live.jpg')
        cv2.imwrite(path+'/live.jpg',frame_read.frame)
        time.sleep(1/30)