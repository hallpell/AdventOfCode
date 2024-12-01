import fileinput

lst1 = []
lst2 = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    stuff = line.split()
    lst1.append(int(stuff[0]))
    lst2.append(int(stuff[1]))

lst1.sort()
lst2.sort()

total = 0

for i in range(len(lst1)):
    total += abs(lst1[i]-lst2[i])

print(total)
