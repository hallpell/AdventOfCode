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
processedIds = set()
src = len(d)-1
while src > 0:
    while d[src] == -1:
        src -= 1
        if src < 0:
            break
    if src < 0:
        break
    id = d[src]
    if id%100 == 0:
        print('pos:', src, 'id:', id)
    if id in processedIds:
#        print('skipping', id)
        src -= 1
        continue
    processedIds.add(id)

    l = 1
    while d[src-1] == id:
        src -= 1
        l += 1
        
    dest = 0
    destLen = 0
    while src > dest:
        if d[dest] == -1:
            destLen += 1
            if l == destLen:
#                print(d)
                for i in range(l):
#                    print(dest-l+1+i, 'from', src + i, "(val overwrote:", d[dest-l+1+i], "val moved:", d[src + i], ")")
                    d[dest-l+1+i] = d[src + i]
                    d[src + i] = -1
#                print(d)
#                print("Moved", l)
                break
        else:
            destLen = 0
        dest += 1
    src -= 1
    
#print(len(d), src, dest)
#print(d[:30])
#print(d[src-10:src+10])
"""for c in d:
    if c == -1:
        print('.', end='')
    else:
        print(c, end='')
print()"""
total = 0
for i in range(len(d)):
    if d[i] == -1:
        continue
    total += d[i] * i

print(total)
