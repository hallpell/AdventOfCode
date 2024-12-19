import fileinput
import time

walls = {}
counter = 0
size = 71
totalInput = 1024

wallsToAdd = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    wallsToAdd.append(line)


def addToPq(pq, val):
    if len(pq) == 0:
        pq.append(val)
    i = 0
    while i < len(pq) and pq[i][-1] > val[-1]:
        i+=1
    pq.append(val)
    return

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

tic = time.time()
for i in range(len(wallsToAdd)):
    walls[wallsToAdd[i]] = 1
    if i < totalInput:
        continue
    pq = [(0,0,0)]
    visited = {"0,0":0}

    best = False
    while len(pq) > 0:
        cur = pq.pop(0)
        x = cur[0]
        y = cur[1]
        steps = cur[2]
        if x == size-1 and y == size-1:
            if best == False or steps < best:
                best = steps
                
        for d in dirs:
            if x + d[0] < 0 or x + d[0] >= size or \
               y + d[1] < 0 or y + d[1] >= size:
                continue
            key = str(x+d[0]) + "," + str(y+d[1])
            if key in walls:
                continue
            if key in visited and visited[key] <= steps+1:
                continue
            addToPq(pq, (x+d[0], y+d[1], steps+1))
            visited[key] = steps
    if best == False:
        print(i)
        print(wallsToAdd[i])
        break
    elif i % 100 == 0:
        print(i, time.time()-tic)
