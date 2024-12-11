import fileinput

grid = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    newRow = []
    for c in line:
        newRow.append(int(c))
    grid.append(newRow)

def createKey(r,c):
    return str(r) + ":" + str(c)

def decodeKey(key):
    return [int(key.split(":")[0]), int(key.split(":")[1])]
    
def getScore(grid, row, col):
    curVal = grid[row][col]
    if curVal == 9:
        return 1
    dirs = [[0,1],[0,-1],[-1,0],[1,0]]
    retVal = 0
    for d in dirs:
        if row+d[0] >= 0 and row+d[0] < len(grid) and \
           col+d[1] >= 0 and col+d[1] < len(grid[0]) and \
           grid[row+d[0]][col+d[1]] == curVal + 1:
            retVal += getScore(grid, row+d[0], col+d[1])
    return retVal
"""    curPos = {}
    curPos[createKey(row,col)] = 1
    for curVal in range(1,10):
        nextPos = {}
        for pKey in curPos.keys():
            p = decodeKey(pKey)
            if p[0] - 1 >= 0 and grid[p[0]-1][p[1]] == curVal:
                nextPos[createKey(p[0]-1, p[1])] = 1
            if p[0] + 1 < len(grid) and grid[p[0]+1][p[1]] == curVal:
                nextPos[createKey(p[0]+1, p[1])] = 1
            if p[1] - 1 >= 0 and grid[p[0]][p[1]-1] == curVal:
                nextPos[createKey(p[0], p[1]-1)] = 1
            if p[1] + 1 < len(grid) and grid[p[0]][p[1]+1] == curVal:
                nextPos[createKey(p[0], p[1]+1)] = 1
        curPos = nextPos
    return len(curPos)"""
    
totalScores = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            score = getScore(grid, i, j)
            totalScores += score
            
print(totalScores)
