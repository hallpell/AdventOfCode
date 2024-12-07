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
            row.append([])
        elif c == '#':
            row.append(1)
        else:
            row.append([c])
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

def prettyPrint(grid):
    for r in grid:
        print(r)
def deepCopy(g):
    newGrid = []
    for r in g:
        newR = []
        for v in r:
            if v == 1:
                newR.append(1)
            elif v == []:
                newR.append([])
            else:
                newR.append([v[0]])
        newGrid.append(newR)
    return newGrid

def countStuck(grid, playerRow, playerCol, playerDirS):
    x = 0
    while True:
        x += 1
        nextR = playerRow + dirDict[playerDirS][0]
        nextC = playerCol + dirDict[playerDirS][1]
        if nextR < 0 or nextR >= len(grid) or nextC < 0 or nextC >= len(grid[0]):
            break
        if grid[nextR][nextC] == 1:
            playerDirS = turnRight(playerDirS)
        else:
            if playerDirS in grid[nextR][nextC]:
#                print(x, nextR, nextC, playerDirS)
                return True
            playerRow = nextR
            playerCol = nextC
            grid[nextR][nextC].append(playerDirS)
    return False

myCounter = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == []:
            grid[r][c] = 1
            if countStuck(deepCopy(grid), playerRow, playerCol, playerDirS):
                myCounter += 1
                print(myCounter, r,c)
            grid[r][c] = []
#            prettyPrint(grid)
print(myCounter)
        
