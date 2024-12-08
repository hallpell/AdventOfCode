import fileinput

grid = []
numRows = 0
numCols = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    grid.append(line)
    numCols = len(line)

numRows = len(grid)

nodes = {}
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '.':
            if grid[r][c] not in nodes:
                nodes[grid[r][c]] = []
            nodes[grid[r][c]].append((r,c))

antis = set()
            
for name in nodes.keys():
    locs = nodes[name]
#    print(len(locs), locs)
    for i in range(len(locs)):
        for j in range(i+1,len(locs)):
#            print(i,j)
            difR = locs[i][0] - locs[j][0]
            difC = locs[i][1] - locs[j][1]
            row = locs[j][0] - difR
            col = locs[j][1] - difC
            antis.add((locs[i][0], locs[i][1]))
            antis.add((locs[j][0], locs[j][1]))
            while not (row < 0 or row >= numRows or col < 0 or col >= numCols):
                antis.add((row, col))
                row -= difR
                col -= difC
            row = locs[i][0] + difR
            col = locs[i][1] + difC
            while not (row < 0 or row >= numRows or col < 0 or col >= numCols):
                antis.add((row, col))
                row += difR
                col += difC
                

#print(nodes)
#print(antis)
#baseGrid = []
#for l in range(len(grid)):
#    newRow = '.' * numCols
#    baseGrid.append(newRow)
#for x in antis:
#    print(x)
#    baseGrid[x[0]] = baseGrid[x[0]][0:x[1]] + "#" + baseGrid[x[0]][x[1]+1:]
##print(len(antis))
#for q in baseGrid:
#    print(q)
total = 0
            
for a in antis:
    if not (a[0] < 0 or a[0] >= numRows or a[1] < 0 or a[1] >= numCols):
#        print(a)
        total += 1

print(total)
