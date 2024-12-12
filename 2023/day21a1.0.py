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

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

def iterate(grid):
    newGrid = []

    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[0])):
            newRow.append(grid[i][j])
        newGrid.append(newRow)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                for d in dirs:
                    if i+d[0] >= 0 and i+d[0] < len(grid) and \
                       j+d[1] >= 0 and j+d[1] < len(grid[0]) and \
                       grid[i+d[0]][j+d[1]] == 0:
                        newGrid[i+d[0]][j+d[1]] = 2
                newGrid[i][j] = 0
    return newGrid

def prettyPrint(grid):
    for r in grid:
        for c in r:
            if c == 0:
                print(".", end='')
            elif c == 1:
                print("#", end='')
            elif c == 2:
                print("O", end='')
            else:
                print("???")
        print()

def count(grid):
    x = 0
    for r in grid:
        for v in r:
            if v == 2:
                x += 1
    return x
        
for i in range(64):
    grid = iterate(grid)
    if i == 5:
        print(i)
        prettyPrint(grid)
        print(count(grid))

print(i)
prettyPrint(grid)
print(count(grid))

