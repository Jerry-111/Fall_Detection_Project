#falling frames
import pandas as pd
import os

fileName = "falling_frames.txt"
f = open(fileName, "r")
lineList = f.readlines()

rangeList = []
for s in lineList:
    s = s[:-1]
    subList = s.split()
    for i in range(1, len(subList)):
        subList[i] = int(subList[i])
    rangeList.append(subList)
rangeList = rangeList[:-2]

df = pd.DataFrame()
df["is_falling"] = []

for cID in range(1,25):
    
    
rNum = rangeList[r][0]
rStart = rangeList[r][1]
rEnd = rangeList[r][2]
    