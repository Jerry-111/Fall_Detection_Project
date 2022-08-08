import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time
import pandas as pd

# cv2.namedWindow('video sequence')

df = pd.DataFrame()
df["moving_pixels"] = []

video_path = "../MHI_1_datas/testData1/cam"
currentFrame = 1

# for camN in range(1,3):
chuteID = 10
camN = 3

# print(cam_path)
# /Fall_Detection/all_frames/chute01/Cam1
# /Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute14/Cam1/frame1071.jpg
# while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):

# currentFrame = 500


def get_acceleration(cam_path, currentFrame):
    img = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
    # print(len(img))
    img = img.reshape(-1)
    cnt = 0
    for i in range(0, len(img), 3):
        if img[i] != 0 and img[i] != 255:
            cnt += 1
    result = round(cnt / 345600 * 100, 4)
    return result


ind = 0
for cID in range(1, 25):
    chuteID = str(cID)
    if len(chuteID) < 2:
        chuteID = "0" + chuteID
    base_path = "../MHI_20_datas/chute" + str(chuteID) + "/Cam"
    for camID in range(1, 9):
        if chuteID == "01":
            camID = 2
        cam_path = base_path + str(camN)
        arr = os.listdir("/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute" + str(chuteID) + "/Cam" + str(camN) + "/")
        aLength = len(arr)
        df = df.append([[] for _ in range(aLength)], ignore_index=True)

        for currentFrame in range(1, aLength):
            if currentFrame > 20:
                result = get_acceleration(cam_path, currentFrame)
                df.at[ind + currentFrame, "moving_pixels"] = result
            elif currentFrame == 1:
                result21 = get_acceleration(cam_path, 21)
                df.at[ind + currentFrame, "moving_pixels"] = 0.5
            else:
                df.at[ind + currentFrame, "moving_pixels"] = result21 / 21 * currentFrame
        ind += aLength

df.to_csv(r"/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/Feature_Extraction/acceleration.csv", index=True)

    # print("cnt:", cnt, result)

# print(len(img))
# cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()