import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time
from skimage.filters import sobel



def keyPoints(img, times):
    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(img,None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    # draw only keypoints location,not size and orientation
    img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
    pts = np.asarray([[round(p.pt[0],1), round(p.pt[1],1)] for p in kp])
    # print(pts)
    # if times == 1:
    #     first_pts = pts
    # else:
    #     second_pts = pts
    plt.imshow(img2), plt.show()

    return pts


def draw_same_keypoints(img, samePoints):
    input_kp = samePoints
    orb = cv2.ORB_create()
    kp, des = orb.compute(img, input_kp)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255,255,0), flags=0)
    plt.imshow(img2)
    plt.show()


def comp_points(first_pts, second_pts, dis):
    # samePoints = np.empty([1,2])
    samePoints = []
    final_pts = []
    for i in range(len(first_pts)):
        for j in range(len(second_pts)):
            if abs(first_pts[i][0] - second_pts[j][0]) <= dis and abs(first_pts[i][1] - second_pts[j][1]) <= dis:
                # print(first_pts[i])
                x, y = first_pts[i]
                samePoints.append((x, y))
                final_pts.append(cv2.KeyPoint(x, y, 1))
                # cv2.KeyPoint(x, y, 1)
                continue
    return samePoints, final_pts


def is_close(p1, p2, dis):
    if (p1[0] - p2[0]) <= dis and (p1[1] - p2[1]) <= dis:
        return True
    return False


cv2.namedWindow('video sequence')

video_path = "../MHI_1_datas/testData1/cam"
currentFrame = 1

# for camN in range(1,3):
camN = 5
cam_path = "../all_frames/chute01/Cam" + str(camN)
# /Fall_Detection/all_frames/chute01/Cam1
# /Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute14/Cam1/frame1071.jpg
# while (os.path.isfile(cam_path + "/frame" + str(currentFrame) + ".jpg")):

currentFrame = 1050
img = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
# img = cv2.GaussianBlur(img, (45,45), cv2.BORDER_DEFAULT)
# img = cv2.GaussianBlur(img, (33,33), cv2.BORDER_DEFAULT)
# img = cv2.GaussianBlur(img, (27,27), cv2.BORDER_DEFAULT)
img = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# global first_pts
# first_pts = np.array([])
first_pts = keyPoints(img, 1)




cam_path = "../MHI_20_datas/chute01/Cam" + str(camN)
# img2 = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
img2 = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
# img2 = sobel(img2)

img2 = cv2.GaussianBlur(img2, (21,21), cv2.BORDER_DEFAULT)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

second_pts = keyPoints(img2, 2)




cam_path = "../MHI_1_datas/chute01/Cam" + str(camN)
img3 = cv2.imread((cam_path + "/frame" + str(currentFrame) + ".jpg"))
img3 = cv2.GaussianBlur(img3, (21,21), cv2.BORDER_DEFAULT)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# global second_pts
# second_pts = np.array([])
third_pts = keyPoints(img3, 2)




samePoints, final_pts = comp_points(first_pts, second_pts, dis=20)
samePoints = list(set(samePoints))
print(len(first_pts), len(second_pts), len(samePoints))
samePoints, final_pts = comp_points(samePoints, third_pts, dis=20)

draw_same_keypoints(img3, final_pts)

# cv2.imshow('MHI Sequence', mhi)
# currentFrame += 1


cv2.waitKey(0)
cv2.destroyAllWindows()