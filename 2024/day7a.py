import fileinput

total = 0

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    nums = line.split()
    goal = int(nums[0][:-1])
#    ops = [0] * (len(nums)-2)
    for i in range(2**(len(nums)-2)):
        ops = bin(i)
        ops = ops[0:2] + '0' * (len(nums)-len(ops)) + ops[2:]
        num = int(nums[1])
        for j in range(len(ops)-2):
            if ops[j+2] == '0':
                num += int(nums[j+2])
            else:
                num *= int(nums[j+2])
        if num == goal:
            total += goal
            break

print(total)
