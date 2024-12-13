import fileinput

a = []
b = []
p = []

totalTokens = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if len(line) < 2:
        continue
    if a == []:
        h = line.split("+")
        a = [int(h[1].split(",")[0]), int(h[2])]
    elif b == []:
        h = line.split("+")
        b = [int(h[1].split(",")[0]), int(h[2])]
    elif p == []:
        h = line.split("=")
        p = [int(h[1].split(",")[0]), int(h[2])]
        best = False
        for aP in range(101):
            for bP in range(101):
                if (p[0] == (aP * a[0] + bP * b[0])) and (p[1] == (aP * a[1] + bP * b[1])):
                    t = aP * 3 + bP
                    if best == False or t < best:
                        best = t
                        bestAP = aP
                        bestBP = bP
        if best != False:
            print(a,b,p,best, bestAP, bestBP)
            totalTokens += best
        

        p = []
        a = []
        b = []
print(totalTokens)
