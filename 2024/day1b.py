import fileinput

lst1 = []
dict2 = {}

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    stuff = line.split()
    lst1.append(int(stuff[0]))
    if int(stuff[0]) not in dict2:
        dict2[int(stuff[0])] = 0
    if int(stuff[1]) not in dict2:
        dict2[int(stuff[1])] = 0
    dict2[int(stuff[1])] += 1

lst1.sort()

total = 0

for i in range(len(lst1)):
    total += lst1[i] * dict2[lst1[i]]

print(total)
