import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

cv2.namedWindow('video sequence')

video_path = "../MHI_1_datas/testData1/cam"
currentFrame = 1

# for camN in range(1,3):
chuteID = 10
camN = 3
if str(chuteID) < 2:
    chuteID = "0" + str(chuteID)
cam_path = "../MHI_20_datas/chute" + str(chuteID) + "/Cam" + str(camN)
# /Fall_Detection/all_frames/chute01/Cam1
# /Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute14/Cam1/frame1071.jpg
# while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):

currentFrame = 1550
img = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
print(len(img))
img = img.reshape(-1)
cnt = 0 
for i in range(0, len(img), 3):
    if 1 < img[i] < 254:
        cnt += 1
result = round(cnt / 345600 * 100,4)
print("cnt:", cnt, result)
# print(len(img))
cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()