import fileinput

total = 0

# from https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    nums = line.split()
    goal = int(nums[0][:-1])
#    ops = [0] * (len(nums)-2)
    for i in range(3**(len(nums)-2)):
        ops = ternary(i)
        ops = '0' * (len(nums)-len(ops)) + ops
        num = int(nums[1])
        for j in range(len(ops)-2):
            if ops[j+2] == '0':
                num += int(nums[j+2])
            elif ops[j+2] == '1':
                num *= int(nums[j+2])
            else:
                num = int(str(num) + str(nums[j+2]))
        if num == goal:
            total += goal
            break


print(total)
