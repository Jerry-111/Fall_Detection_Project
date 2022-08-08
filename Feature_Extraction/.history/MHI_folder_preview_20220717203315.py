import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('video sequence')

video_path = "../MHI_20_datas/testData1/cam"
currentFrame = 1

for N in range(1,3):
    camN = 1
    cam_path = "../MHI_20_datas/testData1/cam" + str(camN)
    while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):
        mhi = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
        # cv2.imshow('MHI Sequence', mhi)
        # currentFrame += 1
        

cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('simple.jpg',0)
