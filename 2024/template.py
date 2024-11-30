import fileinput

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    
