import fileinput

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
        ps = line.split(":")[1].split(",")
        program = []
        for p in ps:
            program.append(int(p))

"""A = 0
B = 29
C = 0
program = [1,7]"""
            
def decode(n):
    if n <= 3:
        combo = program[i+1]
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
    
            
out = []
i = 0
while i < len(program):
    if program[i] == 0:
        combo = decode(program[i+1])
        A = A // (2**combo)
    elif program[i] == 1:
        B = B ^ program[i+1]
    elif program[i] == 2:
        combo = decode(program[i+1])
        B = combo % 8
    elif program[i] == 3:
        if A != 0:
            i = program[i+1] - 2
    elif program[i] == 4:
        B = B ^ C
    elif program[i] == 5:
        out.append(decode(program[i+1])%8)
    elif program[i] == 6:
        combo = decode(program[i+1])
        B = A // (2**combo)
    elif program[i] == 7:
        combo = decode(program[i+1])
        C = A // (2**combo)
    i += 2

s = ''
for v in out:
    s += str(v) + ","
print(s[:-1])
