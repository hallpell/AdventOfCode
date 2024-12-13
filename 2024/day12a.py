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
        if cur[0]-1 < 0 or grid[cur[0]-1][cur[1]] != curV:
            perim += 1
        elif cur[0]-1 >= 0 and up not in visited:
            queue.append(up)
            visited[up] = 1

        if cur[0]+1 >= len(grid) or grid[cur[0]+1][cur[1]] != curV:
            perim += 1
        elif cur[0]+1 < len(grid) and down not in visited:
            queue.append(down)
            visited[down] = 1

        if cur[1]-1 < 0 or grid[cur[0]][cur[1]-1] != curV:
            perim += 1
        elif cur[1]-1 >= 0 and left not in visited:
            queue.append(left)
            visited[left] = 1

        if cur[1]+1 >= len(grid[0]) or grid[cur[0]][cur[1]+1] != curV:
            perim += 1
        elif cur[1]+1 < len(grid) and right not in visited:
            queue.append(right)
            visited[right] = 1
    for p in visited.keys():
        usedGrid[p[0]][p[1]] = 1
    return area * perim

total = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if usedGrid[r][c] == 0:
            total += compute(grid, usedGrid, r, c)
#            print(total, grid[r][c])

print(total)
