import re #For RegEx

total = 0
regex = r"mul\(\d+,\d+\)"

with open("day3-input.txt","r") as file:
    for line in file:
        regexArr = re.findall(regex, line)
        for item in regexArr:
            strippedItem = re.sub(r"[^0-9,]", "", item)
            splitItemArr = strippedItem.split(",")
            num1 = int(splitItemArr[0])
            num2 = int(splitItemArr[1])
            total += num1 * num2
print(total)