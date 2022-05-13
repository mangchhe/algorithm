def dfs(opCnt, nums):
    global maxAns
    global minAns
    if len(nums) > N:
        num = ''.join(map(str, nums))
        maxAns = max(maxAns, num)
        minAns = min(minAns, num)
        return

    for i in range(10):
        if not nums or (calculate(nums[-1], i, op[opCnt]) and i not in nums):
            nums.append(i)
            dfs(opCnt + 1, nums)
            nums.pop()

def calculate(a, b, op):
    if op == '<':
        if a < b:
            return 1
    else:
        if a > b:
            return 1
    return 0

N = int(input())
op = input().split()
maxAns = '0'
minAns = '9999999999'

dfs(-1, [])

print(maxAns)
print(minAns)
