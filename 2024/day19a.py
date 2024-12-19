import fileinput

patterns = []

valid = 0
def isValid(patterns, desire):
    if len(desire) == 0:
        return True
    for p in patterns:
        if p == desire[:len(p)]:
            if isValid(patterns, desire[len(p):]):
                return True
    return False

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if patterns == []:
        patterns = line.split(', ')
        continue
    elif len(line) < 1:
        continue
    if isValid(patterns, line):
        valid += 1
print(valid)
