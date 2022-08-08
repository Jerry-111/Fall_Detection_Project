import cv2
import os

video_path = "../MHI_20_datas/testData1/cam"
currentFrame = 1

for camN in range(1,2):
    cam_path = "../MHI_20_datas/testData1/cam" + str(camN)
    while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):
        mhi = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
        cv2.imshow('MHI Sequence', mhi)
        currentFrame += 1

cv2.waitKey(0)
cv2.destroyAllWindows()
        