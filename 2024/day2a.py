import fileinput

safe = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]

    svals = line.split()
    vals = []
    for s in svals:
        vals.append(int(s))
    cur = vals[0]
    if cur > vals[1]:
        dir = -1
    else:
        dir = 1

    flag = True
    for val in vals[1:]:
        if dir == 1 and val > cur and val <= cur + 3:
            cur = val
        elif dir == -1 and val < cur and val >= cur - 3:
            cur = val
        else:
            flag = False
            break
    if flag:
        safe += 1

print(safe)
    
