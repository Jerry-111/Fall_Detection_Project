import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('video sequence')

video_path = "../all_frames/testData1/cam"
currentFrame = 1

# for camN in range(1,3):
camN = 1
cam_path = "../all_frames/chute01/Cam" + str(camN)
# /Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute14/Cam1/frame1071.jpg
# while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):

currentFrame = 1200
img = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('MHI Sequence', mhi)
# currentFrame += 1

# Initiate ORB detector

                
        

cv2.waitKey(0)
cv2.destroyAllWindows()