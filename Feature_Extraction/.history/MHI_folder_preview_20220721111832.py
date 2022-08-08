import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

def keyPoints(img):
    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(img,None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    # draw only keypoints location,not size and orientation
    img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
    plt.imshow(img2), plt.show()

cv2.namedWindow('video sequence')

video_path = "../MHI_1_datas/testData1/cam"
currentFrame = 1

# for camN in range(1,3):
camN = 1
cam_path = "../MHI_1_datas/chute01/Cam" + str(camN)
# /Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute14/Cam1/frame1071.jpg
# while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):

currentFrame = 1090
img = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
img = cv2.GaussianBlur(img, (45,45), cv2.BORDER_DEFAULT)
img = cv2.GaussianBlur(img, (23,23), cv2.BORDER_DEFAULT)
img = cv2.GaussianBlur(img, (13,13), cv2.BORDER_DEFAULT)
img = cv2.GaussianBlur(img, (13,13), cv2.BORDER_DEFAULT)


# keyPoints(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
keyPoints(img)

# cv2.imshow('MHI Sequence', mhi)
# currentFrame += 1



                
        

cv2.waitKey(0)
cv2.destroyAllWindows()