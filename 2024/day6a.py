import fileinput

grid = []

rowNum = 0
for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    row = []
    colNum = 0
    for c in line:
        
        if c == '.':
            row.append(0)
        elif c == '#':
            row.append(1)
        else:
            row.append(2)
            playerRow = rowNum
            playerCol = colNum
            playerDirS = c
        colNum += 1
    rowNum += 1
    grid.append(row)

def turnRight(dirS):
    if dirS == '^':
        return ">"
    elif dirS == '>':
        return "v"
    elif dirS == "v":
        return "<"
    elif dirS == "<":
        return "^"
    else:
        print("Problem:" + dirS)
dirDict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
counter = 1 # 1 cause we already counted the starting location
while True:
    nextR = playerRow + dirDict[playerDirS][0]
    nextC = playerCol + dirDict[playerDirS][1]
    if nextR < 0 or nextR >= len(grid) or nextC < 0 or nextC >= len(grid[0]):
        break
    if grid[nextR][nextC] == 1:
        playerDirS = turnRight(playerDirS)
    elif grid[nextR][nextC] == 0:
        grid[nextR][nextC] = 2
        playerRow = nextR
        playerCol = nextC
        counter += 1
    elif grid[nextR][nextC] == 2:
        playerRow = nextR
        playerCol = nextC
    else:
        print("Problem!!!")
print(counter)
