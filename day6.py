import numpy as np

def indexSearch(matrix):
    for rowIndex, row in enumerate(matrix):
        for colIndex, element in enumerate(row):
            if element == "^":
                return(colIndex, rowIndex)

matrixCreated = False
angle = 0 # 0=N, 90=E, 180=S, 270=W
distinctPositions = 1
visited = set()

with open("day6-input.txt","r") as file: 
    for line in file:
        line = line.strip()
        row = [str(char) for char in line]
        if matrixCreated:
            matrix = np.vstack((matrix, row))
        else:
            matrix = np.array(row)
            matrixCreated = True

x,y = indexSearch(matrix) # start position
visited.add((x,y))

while 0 <= x <= len(matrix)-1 and 0 <= y <= len(matrix)-1:
    if angle == 0:
        if y - 1 >= 0:
            item = matrix[y-1][x]
            if item == "." and (x,y-1) not in visited:
                visited.add((x,y-1))
            if item != "#":
                y -= 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 90:
        if x + 1 <= len(matrix) - 1:
            item = matrix[y][x+1]
            if item == "." and (x+1,y) not in visited:
                visited.add((x+1,y))
            if item != "#":
                x += 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 180:
        if y + 1 <= len(matrix) - 1:
            item = matrix[y+1][x]
            if item == "." and ((x,y+1)) not in visited:
                visited.add((x,y+1))
            if item != "#":
                y += 1
            else:
                angle = (angle + 90) % 360
        else:
            break
    elif angle == 270:
        if x - 1 >= 0:
            item = matrix[y][x-1]
            if item == "." and (x-1,y) not in visited:
                visited.add((x-1,y))
            if item != "#":
                x -= 1
            else:
                angle = (angle + 90) % 360
        else:
            break
print(len(visited))
