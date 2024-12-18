import fileinput
import time

A = 0
B = 0
C = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    if line[0:3] == 'Reg':
        h = line.split(":")
        if h[0][-1] == 'A':
            A = int(h[1])
        elif h[0][-1] == 'B':
            B = int(h[1])
        elif h[0][-1] == 'C':
            C = int(h[1])
    elif line[0:3] == "Pro":
        ps = line.split(":")[1][1:]
        program = []
        for p in ps.split(","):
            program.append(int(p))

"""A = 0
B = 29
C = 0
program = [1,7]"""
            
def decode(n,A,B,C):
    if n <= 3:
        combo = n
    elif n == 4:
        combo = A
    elif n == 5:
        combo = B
    elif n == 6:
        combo = C
    elif n == 7:
        combo = -1
        print("error: 7 as operand")
    return combo
    
def runProg(A,B,C,program,short=True):
    starts = {}
    out = []
    i = 0
    while i < len(program)-1:
        key = str(A) + ":" + str(B) + ":" + str(C) + ":" + str(i)
        if key in starts:
            return False
        starts[key] = 1
        if program[i] == 0:
            combo = decode(program[i+1],A,B,C)
            A = A // (2**combo)
        elif program[i] == 1:
            B = B ^ program[i+1]
        elif program[i] == 2:
            combo = decode(program[i+1],A,B,C)
            B = combo % 8
        elif program[i] == 3:
            if A != 0:
                i = program[i+1] - 2
        elif program[i] == 4:
            B = B ^ C
        elif program[i] == 5:
            combo = decode(program[i+1],A,B,C)
            out.append(combo%8)
            if not short:
                pass
#                print(combo%8,A,B,C,sep=':')
            if short and out != program[:len(out)]:
                return False
        elif program[i] == 6:
            combo = decode(program[i+1],A,B,C)
            B = A // (2**combo)
        elif program[i] == 7:
            combo = decode(program[i+1],A,B,C)
            C = A // (2**combo)
        i += 2

    s = ''
    for v in out:
        s += str(v) + ","
    return s[:-1]

tic = time.time()
startV = 35184372088832
endV =  281474976710656
for i in range(1000000000,endV-startV):
    if i%100000==0:
        out = runProg(i+startV, B, C, program,False)
    else:
        out = runProg(i+startV, B, C, program,True)
    if out == ps:
        print(i+startV)
        break
        """    elif out != False and len(out) < len(ps):
        print(i, out)
        i *= 2
    elif out != False and len(out) > len(ps):
        print(i, out)
        i = int(i/3)"""
        """else:
        print(i, out)
        x = ''#input()
        if x == '':
            i += 1
        elif x == 'p':
            print(firstOut)
        else:
            i = int(x)"""
    if i % 1000000 == 0:
        print(i, "%", i/(endV-startV), time.time()-tic, out)

#print(runProg(117440, B, C, program)==ps)
