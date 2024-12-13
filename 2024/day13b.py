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
        p = [int(h[1].split(",")[0])+10000000000000, int(h[2])+10000000000000]
        best = False
        bP = round((p[1] - (a[1]*p[0])/a[0]) * a[0] / (a[0]*b[1] - b[0]*a[1]))
        aP = round((p[0] - b[0] * bP)/a[0])
        if p[0] == a[0] * aP + b[0] * bP and p[1] == a[1] * aP + b[1] * bP:
            best = 3*aP + bP
        else:
            pass
            #print("Could not solve", a, b, p)
        if best != False:
            totalTokens += best
        

        p = []
        a = []
        b = []
print(totalTokens)
