import fileinput

finalPs = []
#width = 11
#height = 7
width = 101
height = 103
robots = []

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
    robots.append([p,v])
    
    pf = [(p[0] + v[0] * 100) % width, (p[1] + v[1]*100) % height]
    finalPs.append(pf)

def getPos(p, v, s):
    return [(p[0] + v[0] * s) % width, (p[1] + v[1]*s) % height]
    
def prettyPrint(ps):
    for i in range(height):
        for j in range(width):
            k = str(i)+":"+str(j)
            if k not in ps:
                print(".", end='')
            elif ps[k] < 10:
                print(ps[k], end='')
            else:
                print("#", end='')
        print()

seconds = 0
while True:
    seconds += 1
    print(seconds)
    ps = {}
    for r in robots:
        p = getPos(r[0], r[1], seconds)
        k = str(p[0]) + ":" + str(p[1])
        if k not in ps:
            ps[k] = 0
        ps[k] += 1
    prettyPrint(ps)
    s = input()
    if len(s) > 1:
        seconds = int(s)
    print()
    print()
