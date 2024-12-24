blockArr = []
currentValue = 0
freeSpace = False
checksum = 0

with open("day9-input.txt","r") as file:
    lineArr = file.readlines()
    lineStr = ''.join(str(char) for char in lineArr)
    for char in lineStr:
        if not freeSpace:
            blockArr.extend([currentValue]*int(char))
            currentValue += 1
            freeSpace = True
            
        else:
            blockArr.extend(["."]*int(char))
            freeSpace = False

while "." in blockArr:
    while blockArr[-1] == ".":
        blockArr.pop()
    while blockArr[-1] != "." and "." in blockArr:
        insertionIndex = blockArr.index(".")
        workingValue = blockArr[-1]
        blockArr[insertionIndex] = workingValue
        blockArr.pop()

for index, value in enumerate(blockArr):
    product = index * value
    checksum += product
print(checksum)
