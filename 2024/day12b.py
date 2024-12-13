import fileinput

grid = []
usedGrid = []
for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    grid.append(line)
    usedLine = [0] * len(line)
    usedGrid.append(usedLine)


def compute(grid, usedGrid, row, col):
    queue = [(row,col)]
    visited = {queue[0]: 1}
    fences = {}
    area = 0
    perim = 0
    while len(queue) > 0:
        cur = queue.pop()
        curV = grid[cur[0]][cur[1]]
        area += 1
        up = (cur[0]-1, cur[1])
        down = (cur[0]+1, cur[1])
        left = (cur[0], cur[1]-1)
        right = (cur[0], cur[1]+1)
        fences[cur] = []
        if cur[0]-1 < 0 or grid[cur[0]-1][cur[1]] != curV:
            fences[cur].append('^') 
        elif cur[0]-1 >= 0 and up not in visited:
            queue.append(up)
            visited[up] = 1

        if cur[0]+1 >= len(grid) or grid[cur[0]+1][cur[1]] != curV:
            fences[cur].append('v')
        elif cur[0]+1 < len(grid) and down not in visited:
            queue.append(down)
            visited[down] = 1

        if cur[1]-1 < 0 or grid[cur[0]][cur[1]-1] != curV:
            fences[cur].append('<')
        elif cur[1]-1 >= 0 and left not in visited:
            queue.append(left)
            visited[left] = 1

        if cur[1]+1 >= len(grid[0]) or grid[cur[0]][cur[1]+1] != curV:
            fences[cur].append('>')
        elif cur[1]+1 < len(grid) and right not in visited:
            queue.append(right)
            visited[right] = 1
    for p in visited.keys():
        usedGrid[p[0]][p[1]] = 1
    bulk = 0
    for f in fences.keys():
        for fenceVal in ['v', '^']:
            if fenceVal in fences[f]:
                perim += 1
                fences[f].remove(fenceVal)
                n = (f[0], f[1]+1)
                while n in fences and fenceVal in fences[n]:
                    fences[n].remove(fenceVal)
                    n = (n[0], n[1]+1)
                n = (f[0], f[1]-1)
                while n in fences and fenceVal in fences[n]:
                    fences[n].remove(fenceVal)
                    n = (n[0], n[1]-1)

        for fenceVal in ['<', '>']:
            if fenceVal in fences[f]:
                perim += 1
                fences[f].remove(fenceVal)
                n = (f[0]+1, f[1])
                while n in fences and fenceVal in fences[n]:
                    fences[n].remove(fenceVal)
                    n = (n[0]+1, n[1])
                n = (f[0]-1, f[1])
                while n in fences and fenceVal in fences[n]:
                    fences[n].remove(fenceVal)
                    n = (n[0]-1, n[1])
    return area * perim

total = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if usedGrid[r][c] == 0:
            total += compute(grid, usedGrid, r, c)
#            print(total, grid[r][c])

print(total)
