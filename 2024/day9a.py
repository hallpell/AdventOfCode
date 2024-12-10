import fileinput

d = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    idCounter = 0
    for i in range(len(line)):
        if i % 2 == 0:
#            print("Adding ", idCounter, int(line[i]), "times")
            d += [idCounter] * int(line[i])
            idCounter += 1
        else:
#            print("Adding -1", int(line[i]), "times")
            d += [-1] * int(line[i])

#print(d[-10:])
src = len(d)-1
while d[src] == -1:
    src -= 1
dest = 0
while d[dest] != -1:
    dest += 1

while src > dest:
    d[dest] = d[src]
    d[src] = -1
    while d[src] == -1:
        src -= 1
    while d[dest] != -1:
        dest += 1

#print(len(d), src, dest)
#print(d[:30])
#print(d[src-10:src+10])
total = 0
for i in range(len(d)):
    if d[i] == -1:
        break
    total += d[i] * i

print(total)
