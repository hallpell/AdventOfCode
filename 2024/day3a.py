import fileinput
import re

total = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    for i in range(len(line)):
        if line[i] == 'm' and re.match('^mul\(\d{1,3},\d{1,3}\)', line[i:]):
            hold = line[i:].split('(')[1].split(')')[0].split(',')
            total += int(hold[0]) * int(hold[1])

print(total)
