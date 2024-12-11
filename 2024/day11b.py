import fileinput
import time

tic = time.time()

nums = []
numsD = {}

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    hold = line.split()
    for n in hold:
        n = int(n)
        if n not in numsD:
            numsD[n] = 0
        numsD[n] += 1

def safeAdd(d, v, n):
    if v not in d:
        d[v] = 0
    d[v] += n
    
def iterate(numsD):
    newNumsD = {}
    for n in numsD.keys():
        if n == 0:
            safeAdd(newNumsD, 1, numsD[n])
        elif len(str(n)) % 2 == 0:
            l = len(str(n))
            v1 = int(str(n)[:l//2])
            safeAdd(newNumsD, v1, numsD[n])
            v2 = int(str(n)[l//2:])
            safeAdd(newNumsD, v2, numsD[n])
        else:
            safeAdd(newNumsD, n*2024, numsD[n])
    return newNumsD

for i in range(76):
    total = 0
    for n in numsD.keys():
        total += numsD[n]
    print(i, len(numsD.keys()), total, time.time()-tic)
    numsD = iterate(numsD)
