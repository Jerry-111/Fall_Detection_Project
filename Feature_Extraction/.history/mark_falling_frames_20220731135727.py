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
        if subList[i] == "-1":
            subList[i] = 9999999
        subList[i] = int(subList[i])
    rangeList[str(subList[0])] = (subList[1], subList[2])
print(rangeList)

df = pd.DataFrame()
df["is_falling"] = []
ind = 0

# for cID in range(1,25):
#     cID = str(cID)
#     if int(cID) < 10:
#         cID = '0' + cID
cID, camN = "14", "1"
    # for camN in range(1,9):


arr = os.listdir("/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute" + str(cID) + "/Cam" + str(camN) + "/")


df = df.append([[] for _ in range(len(arr))], ignore_index=True)
df["is_falling"].values[ind:] = False

for frame in range(len(arr)):
    if int(arr[frame][5:-4]) in range(rangeList[cID][0], rangeList[cID][1]+1):
        # print(arr[frame])
        df.at[int(arr[frame][5:-4]),'is_falling'] = True
print(df[1050:1244])       
# rNum = rangeList[r][0]
# rStart = rangeList[r][1]
# rEnd = rangeList[r][2]
    