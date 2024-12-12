import fileinput

grid = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    newRow = []
    for c in line:
        if c == '.':
            newRow.append(0)
        elif c == '#':
            newRow.append(1)
        elif c == 'S':
            newRow.append(2)
    grid.append(newRow)

#for r in grid:
#    print(r)

def makeKey(r,c):
    return str(r)+":"+str(c)

def decodeKey(k):
    return [int(k.split(":")[0]), int(k.split(":")[1])]

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
obstacles = {}
curPos = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            obstacles[makeKey(i,j)] = 1
        elif grid[i][j] == 2:
            curPos[makeKey(i,j)] = 1
            
def iterate(curPos, obstacles):
    newPos = {}
    for p in curPos:
        [i,j] = decodeKey(p)
        for d in dirs:
            if makeKey(i+d[0],j+d[1]) not in obstacles:
                newPos[makeKey(i+d[0],j+d[1])] = 1
    return newPos

def prettyPrint(curPos, obstacles):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            k = makeKey(i,j)
            if k in obstacles:
                print("#", end='')
            elif k in curPos:
                print("O", end='')
            else:
                print(".", end='')
        print()

for i in range(64):
    curPos = iterate(curPos, obstacles)

print(i)
#prettyPrint(curPos, obstacles)
print(len(curPos.keys()))


