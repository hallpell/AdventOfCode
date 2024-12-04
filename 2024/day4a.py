import fileinput

grid = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    grid.append(line)

word = 'XMAS'
word2 = 'SAMX'

total = 0

for i in range(len(grid)):
    for j in range(len(grid[i])-3):
        x = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]
        if x == word or x == word2:
            total += 1
#            print(i,j, 'h', x)
        x = grid[j][i] + grid[j+1][i] + grid[j+2][i] + grid[j+3][i]
        if x == word or x == word2:
            total += 1
#            print(i,j, 'v', x)
        if i < len(grid[0])-3:
            x = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
            if x == word or x == word2:
                total += 1
#                print(i,j, '-', x)
            x = grid[i+3][j] + grid[i+2][j+1] + grid[i+1][j+2] + grid[i][j+3]
            if x == word or x == word2:
                total += 1
#                print(i,j, '+', x)


print(total)
