#falling frames

fileName = "falling_frames.txt"
f = open(fileName, "r")
lineList = f.readlines()

rangeList = []
for s in lineList:
    s = s[:-1]
    subList = s.split()
    subList = list(map(int, subList[1:]))
    range
    rangeList.append(subList)
print(rangeList)