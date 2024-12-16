import fileinput

grid = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    newRow = []
    for c in line:
        if c == '#':
            newRow.append(0)
        if c == '.' or c == 'E' or c == 'S':
            newRow.append(1)
    grid.append(newRow)

def prettyPrint(grid, p):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            c = grid[x][y]
            if c == 0:
                print('#', end='')
            else:
                if str(x) + ":" + str(y) in p:
                    print("O", end='')
                else:
                    print(".", end='')
        print()

goal = [1,len(grid[1])-2]
start = [len(grid)-2, 1]
#print(grid[start[0]][start[1]], grid[goal[0]][goal[1]])
#prettyPrint(grid)

pq = [(start, '>', [str(start[0])+":"+str(start[1])], 0)]
considered = {str(start[0]) + ":" + str(start[1]) + "@>": 0}
pathsTo = {str(start[0]) + ":" + str(start[1]) + "@>": [str(start[0]) + ":" + str(start[1])]}

def addToPq(pq, val):
    if len(pq) == 0:
        pq.append(val)
    i = 0
    while i < len(pq) and pq[i][-1] > val[-1]:
        i+=1
    pq.append(val)
    return

dirMap = {"v": [1,0], ">": [0,1], "<": [0,-1], "^": [-1,0]}
turnLeft = {"v": ">", ">": "^", "<": "v", "^": "<"}
turnRight = {"v": "<", ">": "v", "<": "^", "^": ">"}

def makeKey(v):
    return str(v[0][0]) + ":" + str(v[0][1]) + "@" + v[1]

score = False
p = False

while len(pq) > 0:
    cur = pq.pop(0)
    x = cur[0][0]
    y = cur[0][1]
    d = cur[1]
    visitedSoFar = cur[2]
    s = cur[3]
    if x == goal[0] and y == goal[1] and (score == False or s < score):
        score = s
        p = visitedSoFar.copy()
    key = makeKey(cur)
    if key not in considered:
        print("Didn't see", key, "before!!!")
    if grid[x+dirMap[d][0]][y+dirMap[d][1]] == 1:
        nextVvisited = visitedSoFar.copy()
        nextVvisited.append(str(x+dirMap[d][0]) + ":" + str(y+dirMap[d][1]))
        nextV = ([x+dirMap[d][0],y+dirMap[d][1]], d, nextVvisited, s+1)
        nextVk = makeKey(nextV)
        if nextVk not in considered or s+1 < considered[nextVk]:
            addToPq(pq, nextV)
            considered[nextVk] = s+1
            pathsTo[nextVk] = nextVvisited
        elif s+1 == considered[nextVk]:
            for z in nextVvisited:
                if z not in pathsTo[nextVk]:
                    pathsTo[nextVk].append(z)

    nextL = ([x,y], turnLeft[d], visitedSoFar, s+1000)
    nextLk = makeKey(nextL)
    if nextLk not in considered or s+1000 < considered[nextLk]:
        addToPq(pq, nextL)
        considered[nextLk] = s+1000
        pathsTo[nextLk] = visitedSoFar

    nextR = ([x,y], turnRight[d], visitedSoFar, s+1000)
    nextRk = makeKey(nextR)
    if nextRk not in considered or s+1000 <= considered[nextRk]:
        addToPq(pq, nextR)
        considered[nextRk] = s+1000
        pathsTo[nextRk] = visitedSoFar

        
#prettyPrint(grid,p)
print(len(p))
#print(p)
