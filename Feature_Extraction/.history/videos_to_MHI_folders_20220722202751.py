import cv2
import numpy as np
from scipy import ndimage as nd
from skimage.filters import sobel
import os


MHI_DURATION = 3
#MHI_DURATION = 20
DEFAULT_THRESHOLD = 32



video_src = 0

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
base_path = "../MHI_1_datas/testData1"

for cID in range(1,25):
    if len(str(cID)) == 1:
        chuteID = "0" + str(cID)
    else:
        chuteID = cID
    base_path = "../all_frames/chute" + str(chuteID)   
        
    for camN in range(1,9):
        video_src = '/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/dataset/chute' + str(chuteID) + '/cam' + str(camN) + '.avi'
        cam = cv2.VideoCapture(video_src)
        ret, frame = cam.read()
        h, w = frame.shape[:2]
        prev_frame = frame.copy()
        motion_history = np.zeros((h, w), np.float32)
        timestamp = 0
        currentFrame = 0

        cam_path = base_path + "/Cam" + str(camN)
        
        while True:
            ret, frame = cam.read()   
            if not ret:
                break
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.fastNlMeansDenoising(frame, None, 30, 7, 21) 
            
            alpha = 1.5 # Contrast control (1.0-3.0)
            beta = 0 # Brightness control (0-100)

            adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
            adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

            cv2.imshow('original', frame)
            cv2.imshow('adjusted', adjusted)
            
            """frame = cv2.GaussianBlur(frame, (3,3), cv2.BORDER_DEFAULT)
            
            frame_diff = cv2.absdiff(frame, prev_frame)
            gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
            
            
            #cv2.fastNlMeansDenoising(gray_diff, None, 40, 7, 21) 
            #gray_diff = cv2.GaussianBlur(gray_diff, (5,5), cv2.BORDER_DEFAULT)
            
            
            ret, fgmask = cv2.threshold(gray_diff, DEFAULT_THRESHOLD, 1, cv2.THRESH_BINARY)
            timestamp += 1
            
            # update motion history
            cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, MHI_DURATION)

            
            # flag += 1
            mh = np.uint8(np.clip((motion_history - (timestamp - MHI_DURATION)) / MHI_DURATION, 0, 1) * 255)"""
            
            # if not os.path.exists(base_path):
            #     os.makedirs(base_path)
            # if not os.path.exists(cam_path):
            #     os.makedirs(cam_path)
            # currentFrame += 1
            # if os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg"):
            #     os.remove(cam_path + "/frame" + str(currentFrame) + ".jpg")
            # cv2.imwrite(cam_path + "/frame" + str(currentFrame) + ".jpg", frame)
            
            """ if flag == 10:
                print(mh[:20][:10])
                flag += 1
                cv2.imshow('mhi', mh)"""
                
            # cv2.imshow('motion-history', mh)
            # cv2.imshow('raw', frame)
            
            

            prev_frame = frame.copy()
            if 0xFF & cv2.waitKey(5) == 27:
                break
                

cv2.destroyAllWindows()