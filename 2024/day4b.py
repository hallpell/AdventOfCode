import fileinput

grid = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    grid.append(line)

total = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):
        if grid[i][j] == 'A':
            y = {grid[i-1][j-1], grid[i+1][j+1]}
            z = {grid[i-1][j+1], grid[i+1][j-1]}
            if y == z and y == {'M', 'S'}:
                total += 1


print(total)
