#falling frames
import pandas as pd
import os

fileName = "falling_frames.txt"
f = open(fileName, "r")
lineList = f.readlines()

rangeList = {}
lineList = lineList[:-2]
for s in lineList:
    s = s[:-1]
    subList = s.split()
    for i in range(1, len(subList)):
        subList[i] = int(subList[i])
    rangeList[str(subList[0])] = (subList[1], subList[2])
print(rangeList)

df = pd.DataFrame()
df["is_falling"] = []

# for cID in range(1,25):
#     cID = str(cID)
#     if int(cID) < 10:
#         cID = '0' + cID
cID, camN = "14", "1"
# for camN in range(1,9):
    arr = os.listdir("/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute" + str(cID) + "/Cam" + str(camN) + "/")
    for frame in range(len(arr)):
        if int(arr[frame][5:-4]) in rangeList[cID]:
            print(arr[frame])
# rNum = rangeList[r][0]
# rStart = rangeList[r][1]
# rEnd = rangeList[r][2]
    