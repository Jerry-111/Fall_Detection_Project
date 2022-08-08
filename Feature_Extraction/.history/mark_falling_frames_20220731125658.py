#falling frames

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
for r in range(rangeList, len(rangeList)):
    rNum = r[0]
    rStart = r[1]
    rEnd = r[2]
    print(rNum, rStart, rEnd)