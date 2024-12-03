safeReports = 0
isIncreasing = ""
with open("day2-input.txt", "r") as allReports:
    for report in allReports:
        safe = True
        isIncreasing = ""
        levelArray = report.strip().split(" ") # each report is made into levels
        for i in range(len(levelArray) - 1):
            a = int(levelArray[i])
            b = int(levelArray[i+1])
            if isIncreasing == "":
                if a < b:
                    isIncreasing = True
                    print(levelArray)
                elif a > b:
                    isIncreasing = False
                else:
                    safe = False
                    # Value is repeated on the very first number
            if isIncreasing:
                if a > b or b-a > 3:
                    safe = False
            else:
                if a < b or b-a < -3:
                    safe = False
            if a == b:
                safe = False
        if safe:
            safeReports += 1
print(safeReports)