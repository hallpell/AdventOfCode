import fileinput

nums = []

for line in fileinput.input():
    if line[-1] == '\n':
        line = line[:-1]
    hold = line.split()
    for n in hold:
        nums.append(int(n))
        
def iterate(nums):
    newNums = []
    for n in nums:
        if n == 0:
            newNums.append(1)
        elif len(str(n)) % 2 == 0:
            l = len(str(n))
            newNums.append(int(str(n)[:l//2]))
            newNums.append(int(str(n)[l//2:]))
        else:
            newNums.append(n*2024)
    return newNums

for i in range(26):
    print(i, len(nums))
    nums = iterate(nums)
