import fileinput

grid = []

inGrid = True
dirs = ""

roboR = roboC = 0
for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if inGrid:
        if len(line) < 2:
            inGrid = False
            continue
        newRow = []
        roboC = 0
        for c in line:
            if c == '#':
                newRow.append(2)
            elif c == 'O':
                newRow.append(1)
            elif c == '@':
                newRow.append(3)
                R = roboR
                C = roboC
            else:
                newRow.append(0)
            roboC += 1
        grid.append(newRow)
        roboR += 1
    else:
        dirs += line

def prettyPrint(grid):
    for row in grid:
        for c in row:
            if c == 2:
                print("#", end='')
            elif c == 1:
                print("O", end='')
            elif c == 3:
                print("@", end='')
            elif c == 0:
                print(".", end='')
        print()

#prettyPrint(grid)

dirsMap = {"^": [-1,0], ">": [0,1], "<": [0,-1], "v": [1,0]}

def move(grid, dir, r,c):
    if grid[r][c] != 3:
        print("Robot missing!!!")
        return
    elif grid[r+dir[0]][c+dir[1]] == 2:
        return [r, c]
    elif grid[r+dir[0]][c+dir[1]] == 0:
        grid[r+dir[0]][c+dir[1]] = 3
        grid[r][c] = 0
        return [r+dir[0], c+dir[1]]
    elif grid[r+dir[0]][c+dir[1]] == 1:
        i = 1
        while grid[r+dir[0]*i][c+dir[1]*i] == 1:
            i += 1
        if grid[r+dir[0]*i][c+dir[1]*i] == 2:
            return [r, c]
        elif grid[r+dir[0]*i][c+dir[1]*i] == 0:
            grid[r+dir[0]*i][c+dir[1]*i] = 1
            grid[r+dir[0]][c+dir[1]] = 3
            grid[r][c] = 0
            return [r+dir[0],c+dir[1]]
        else:
            print("???")
            return
    else:
        print("?!?!?!")
        return

for d in dirs:
    [R, C] = move(grid, dirsMap[d], R, C)

total = 0
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            total += 100*i + j

print(total)
