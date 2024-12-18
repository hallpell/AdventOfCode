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

    return out

def lst2str(lst):
    s = ''
    for v in lst:
        s += str(v) + ","
    return s[:-1]

tic = time.time()
startV = 35184372088832
endV =  281474976710656
outLen = 4
nextStart = 1
for outLen in range(4,len(program)+1):
    for i in range(nextStart,endV):
        out = runProg(i, B, C, program,False)
        if lst2str(out) == lst2str(program[-outLen:]):
            print(outLen, i)
            nextStart = i * 8
            break
#        if i % 1000 == 0:
#            print(i, time.time()-tic, out, program[-outLen:])

#print(runProg(117440, B, C, program)==ps)
# 10:
# 8: 5420377
