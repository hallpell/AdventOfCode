import fileinput
import re

# 47|53 means 47 can't go after 53, so
# read this in as 53 -> [47] 
ir = {}

inRules = True
total = 0

def fix(pages, ir):
    validP = True
    for i in range(len(pages)):
        if pages[i] in ir:
            for invalidPage in ir[pages[i]]:
                if invalidPage in pages[i+1:]:
                    validP = False
                    ind = pages.index(invalidPage)
                    (pages[i], pages[ind]) = (pages[ind], pages[i])
    return validP
                        

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if inRules:
        if len(line) < 2:
#            print(ir)
            inRules = False
            continue
        hold = line.split('|')
        if int(hold[1]) not in ir:
            ir[int(hold[1])] = []
        ir[int(hold[1])].append(int(hold[0]))
    elif not inRules:
        spages = line.split(',')
        pages = []
        for s in spages:
            pages.append(int(s))
        validP = True
        while not fix(pages, ir):
            validP = False
            
        if not validP:
#            print(pages)
            total += pages[int(len(pages)/2)]

print(total)
