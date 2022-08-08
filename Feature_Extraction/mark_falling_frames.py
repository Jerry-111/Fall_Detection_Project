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
    rangeList[str(subList[0])] = subList[1:]
print(rangeList)

df = pd.DataFrame()
df["scene/cam"] = []
df["is_falling"] = []
df['is_falling'] = df['is_falling'].astype('bool')
ind = 0

for cID in range(1,25):
    cID = str(cID)
    if int(cID) < 10:
        cID = '0' + cID

    rStart, rEnd = int(rangeList[cID][0]), int(rangeList[cID][1])+1
    for camN in range(1,9):
        scene_cam_ID = cID + '/' + str(camN)
        arr = os.listdir("/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute" + str(cID) + "/Cam" + str(camN) + "/")

        aLength = len(arr)
        df = df.append([[] for _ in range(aLength)], ignore_index=True)
        df["is_falling"].values[ind:] = False

        for frame in range(aLength):
            df.at[ind + int(arr[frame][5:-4]), "scene/cam"] = scene_cam_ID
            if int(arr[frame][5:-4]) in range(rStart, rEnd):
                df.at[ind + int(arr[frame][5:-4]), "is_falling"] = True
        ind += aLength


print(df)
df.to_csv(r"/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/Feature_Extraction/features.csv", index=True)
    