import fileinput

inRules = True

rulesNums = set()
bookNums = set()
for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if inRules:
        if len(line) < 2:
            inRules = False
            continue
        hold = line.split('|')
        for x in hold:
            rulesNums.add(int(x))

    else:
        hold = line.split(',')
        for x in hold:
            bookNums.add(int(x))
print(bookNums - rulesNums)
print(rulesNums - bookNums)
