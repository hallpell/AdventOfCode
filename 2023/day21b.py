import fileinput
import time

tic = time.time()

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
originalObs = {}
frontier = {}
evens = {}
odds = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            obstacles[makeKey(i,j)] = 1
            originalObs[makeKey(i,j)] = 1
        elif grid[i][j] == 2:
            frontier[makeKey(i,j)] = 1
            evens[makeKey(i,j)] = 1
            
def iterate(frontier, obstacles, old):
    global minR, minC, maxR, maxC, originalObs, expanded
    newFrontier = {}
    for p in frontier.keys():
        [i,j] = decodeKey(p)
        for d in dirs:
            k = makeKey(i+d[0], j+d[1])
            # if we haven't computed obstacles in this portion, do that (all 4 directions)
            if i+d[0] < minR:
#                expanded = True
                mult = (minR//height) - 1
                for a in range(minC//width, maxC//width):
                    for ok in originalObs.keys():
                        [oki, okj] = decodeKey(ok)
                        obstacles[makeKey(oki + mult*height, okj + a*width)] = 1
                minR -= height
#                prettyPrint(old, obstacles)
            if i+d[0] >= maxR:
                expanded = True
                mult = (maxR//height)
                for a in range(minC//width, maxC//width):
                    for ok in originalObs.keys():
                        [oki, okj] = decodeKey(ok)
                        obstacles[makeKey(oki + mult*height, okj + a*width)] = 1
                maxR += height
            if j+d[1] < minC:
#                expanded = True
                mult = (minC//width) - 1
                for a in range(minR//height, maxR//height):
                    for ok in originalObs.keys():
                        [oki, okj] = decodeKey(ok)
                        obstacles[makeKey(oki + a*height, okj + mult*width)] = 1
                minC -= width
            if j+d[1] > maxC:
#                expanded = True
                mult = (maxC//width)
                for a in range(minR//height, maxR//height):
                    for ok in originalObs.keys():
                        [oki, okj] = decodeKey(ok)
                        obstacles[makeKey(oki + a*height, okj + mult*width)] = 1
                maxC += width
            # actually compare to obstacles
            if k not in obstacles:
                if k not in old:
                    newFrontier[k] = 1
                    old[k] = 1
    return newFrontier

def prettyPrint(curPos, obstacles):
    for i in range(-len(grid), len(grid)):
        for j in range(len(grid[0])):
            k = makeKey(i,j)
            if k in obstacles:
                print("#", end='')
            elif k in curPos:
                print("O", end='')
            else:
                print(".", end='')
        print()

def prettyPrint2(front, e, o, obstacles, minR, maxR, minC, maxC):
    for i in range(minR, maxR):
        for j in range(minC, maxC):
            k = makeKey(i,j)
            if k in obstacles:
                print("#",end='')
            elif k in front:
                print("O",end='')
            elif k in e:
                print("e",end='')
            elif k in o:
                print("o",end='')
            else:
                print(".",end='')
        print()
        
minR = minC = 0
height = maxR = len(grid)
width = maxC = len(grid[0])
expanded = False
        
for i in range(100):
    if i % 2 == 0:
        frontier = iterate(frontier, obstacles, odds)
    else:
        frontier = iterate(frontier, obstacles, evens)
# if i in [5, 9, 49, 99, 499, 999, 4999] or i % 100 == 0 or expanded:
    if expanded:
        prettyPrint2(frontier, evens, odds, obstacles, maxR-height*2, maxR, -width, 2*width)
        print(i, len(frontier), len(evens), time.time()-tic)
        expanded = False
print(i)
#prettyPrint(curPos, obstacles)
print(len(evens.keys()))


