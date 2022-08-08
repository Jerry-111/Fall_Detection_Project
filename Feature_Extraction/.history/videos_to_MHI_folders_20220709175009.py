import cv2
import numpy as np
from scipy import ndimage as nd
from skimage.filters import sobel
import os


MHI_DURATION = 5
#MHI_DURATION = 20
DEFAULT_THRESHOLD = 32



live_video = False
video_src = 0
if not live_video:
    # video_src = "E:\Projects\computer-vision\computer-vision-python\opencv-starter\data/video/Sequence_6/visor_1246523090489_new_6_camera1.avi".replace('\\', '/')
    # video_src = "E:\Projects\computer-vision\computer-vision-python\opencv-starter\data/video\AVSS/AVSS_AB_Easy.avi".replace('\\', '/')
    video_src = '/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/dataset/chute01/cam1.avi'

cv2.namedWindow('motion-history')
cv2.namedWindow('raw')
cv2.moveWindow('raw', 200, 0)

cam = cv2.VideoCapture(video_src)
ret, frame = cam.read()
h, w = frame.shape[:2]
prev_frame = frame.copy()
motion_history = np.zeros((h, w), np.float32)
timestamp = 0
# flag = 1
currentFrame = 0


while True:
    ret, frame = cam.read()   
    if not ret:
        break
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.fastNlMeansDenoising(frame, None, 30, 7, 21) 
    
    #frame = cv2.GaussianBlur(frame, (9,9), cv2.BORDER_DEFAULT)
    
    frame_diff = cv2.absdiff(frame, prev_frame)
    gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    
    
    #cv2.fastNlMeansDenoising(gray_diff, None, 40, 7, 21) 
    #gray_diff = cv2.GaussianBlur(gray_diff, (5,5), cv2.BORDER_DEFAULT)
    
    
    ret, fgmask = cv2.threshold(gray_diff, DEFAULT_THRESHOLD, 1, cv2.THRESH_BINARY)
    timestamp += 1
    
    # update motion history
    cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, MHI_DURATION)

    # normalize motion history
    
    # flag += 1
    mh = np.uint8(np.clip((motion_history - (timestamp - MHI_DURATION)) / MHI_DURATION, 0, 1) * 255)
    
    
    
    """ if flag == 10:
        print(mh[:20][:10])
        flag += 1
        cv2.imshow('mhi', mh)"""
        
    cv2.imshow('motion-history', mh)
    cv2.imshow('raw', frame)
    
    

    prev_frame = frame.copy()
    if 0xFF & cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()