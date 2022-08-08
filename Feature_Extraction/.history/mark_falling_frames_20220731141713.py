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
df["is_falling"] = []
ind = 0

# for cID in range(1,25):
#     cID = str(cID)
#     if int(cID) < 10:
#         cID = '0' + cID
cID, camN = "02", "1"
for camN in range(1,9):

    arr = os.listdir("/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/MHI_20_datas/chute" + str(cID) + "/Cam" + str(camN) + "/")

    df = df.append([[] for _ in range(len(arr))], ignore_index=True)
    df["is_falling"].values[ind:] = False
    ind += len(arr)

    for frame in range(len(arr)):
        if int(arr[frame + ind][5:-4]) - ind in range(rStart, rEnd):
            # print(arr[frame])
            df.at[int(arr[ind + frame][5:-4]),'is_falling'] = True
print(df)
df.to_csv(r"/Users/jerrychen/Desktop/PythonWorks/Fall_Detection/Feature_Extraction/features.csv", index=True)
    