#falling frames

fileName = "falling_frames.txt"
f = open(fileName, "r")
lineList = f.readlines()
print(lineList)
rangeList = []
for s in lineList:
    s = s[:-2]
    rangeList.append(s)