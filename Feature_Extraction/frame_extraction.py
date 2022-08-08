import cv2
import os

vid = cv2.VideoCapture("/Users/jerrychen/Downloads/chute01/cam1.avi")
currentFrame = 0

if not os.path.exists("testDataSet"):
    os.makedirs("testDataSet")

while True:
    ret, frame = vid.read()
    
    cv2.imshow("Output", frame)
    cv2.imwrite("/Users/jerrychen/Downloads/testDataSet/frame" + str(currentFrame) + ".jpg", frame)
    currentFrame += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()