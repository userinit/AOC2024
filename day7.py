import itertools

operators = "*+"
totalCalibrations = 0

with open("day7-input.txt","r") as file:
    for line in file:
        answerProductArr = line.split(":")
        answer = answerProductArr[0]
        productStr = answerProductArr[1].strip()
        productArr = productStr.split(" ")
        operatorCombos = [''.join(operator) for operator in itertools.product(operators, repeat=len(productArr)-1)]
        validCalculation = False
        for operatorArr in operatorCombos: # iterates over each operator in the combination
            calculationArr = []
            for i in range(len(productArr)-1):
                calculationArr.append("(")
            for j, operator in enumerate(operatorArr):
                calculationArr.append(productArr[j])
                if j != 0:
                    calculationArr.append(")")
                calculationArr.append(operator)
                if j == len(operatorArr)-1:
                    calculationArr.append(productArr[j+1])
                    calculationArr.append(")")
            calculationStr = ''.join(str(char) for char in calculationArr)
            calculation = eval(calculationStr)
            if calculation == int(answer):
                totalCalibrations += calculation
                break
print(totalCalibrations)
