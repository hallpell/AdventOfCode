import fileinput

walls = {}
counter = 0
size = 71
totalInput = 1024

wallsToAdd = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    walls[line] = 1
    counter += 1
    if counter == totalInput:
        break

pq = [(0,0,0)]
visited = {"0,0":0}

def addToPq(pq, val):
    if len(pq) == 0:
        pq.append(val)
    i = 0
    while i < len(pq) and pq[i][-1] > val[-1]:
        i+=1
    pq.append(val)
    return

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
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
print(best)
