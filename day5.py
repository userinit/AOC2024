import re

rules = []
content = []
middleNumberTotal = 0


with open("day5-input.txt","r") as file:
    for line in file: # adding rules
        if line == '\n':
            break
        else:
            rules.append(line.strip())
    for line in file: # adding content
        if not re.search(r"\|", line):
            content.append(line.strip())

for update in content:
    validUpdate = True
    strUpdateArr = update.split(",")
    updateArr = [int(item) for item in strUpdateArr]
    for rule in rules:
        if not validUpdate:
            break
        ruleArray = rule.split("|")
        ruleNumOne = int(ruleArray[0])
        ruleNumTwo = int(ruleArray[1])
        if ruleNumOne in updateArr and ruleNumTwo in updateArr: # if they are not both present, no need to check rules
            ruleOneIndex = updateArr.index(ruleNumOne)
            ruleTwoIndex = updateArr.index(ruleNumTwo)
            if ruleOneIndex > ruleTwoIndex: # checks if second value in rule is earlier (invalid update)
                validUpdate = False
    if validUpdate:
        middleIndex = int((len(updateArr)-1)/2)
        middleNumber = updateArr[middleIndex]
        middleNumberTotal += middleNumber
print(middleNumberTotal)
