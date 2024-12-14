import fileinput

finalPs = []
#width = 11
#height = 7
width = 101
height = 103

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    h = line.split()
    ph = h[0].split('=')
    vh = h[1].split('=')
    phh = ph[1].split(',')
    vhh = vh[1].split(',')
    p = [int(phh[0]), int(phh[1])]
    v = [int(vhh[0]), int(vhh[1])]

    pf = [(p[0] + v[0] * 100) % width, (p[1] + v[1]*100) % height]
    finalPs.append(pf)

quads = [0,0,0,0]
for pf in finalPs:
    if pf[0] != width//2 and pf[1] != height//2:
        if pf[0] < width//2:
            x = 0
        else:
            x = 1
        if pf[1] < height//2:
            y = 0
        else:
            y = 2
        quads[x+y] += 1

print(quads)
prod = 1
for q in quads:
    prod *= q
print(prod)
