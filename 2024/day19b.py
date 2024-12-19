import fileinput
import functools

patterns = []

valid = 0
@functools.cache
def isValid(desire):
    global patterns
#    print('Entering, D=', desire)
    if len(desire) == 0:
#        print("Early exit")
        return 1
    possible = 0
    for p in patterns:
        if p == desire[:len(p)]:
            possible += isValid(desire[len(p):])
#    print("Exiting, D=", desire, possible)
    return possible

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if patterns == []:
        patterns = line.split(', ')
        continue
    elif len(line) < 1:
        continue
    h = isValid(line)
    valid += h
    print(line, h)
print(valid)
