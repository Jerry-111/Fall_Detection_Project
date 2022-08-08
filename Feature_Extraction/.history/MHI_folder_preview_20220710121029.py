import cv2
import os

video_path = "../MHI_20_datas/testData1/cam"

for camN in range(1,9):
    cam_path = "../MHI_20_datas/testData1/cam" + str(camN) + "/"
    while (os.path.isfile())