#falling frames

fileName = "falling_frames.txt"
f = open(fileName, "r")
lineList = f.readlines()

rangeList = []
for s in lineList:
    s = s[:-1]
    tempList = s.split()
    for i in range(1, len(tempList)):
        subList[i] = str(int(tempList[i]))
    rangeList.append(subList)
print(rangeList)