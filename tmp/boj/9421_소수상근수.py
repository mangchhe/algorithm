from functools import reduce

def erathos(arr):
    for i in range(2, int(len(arr) ** .5) + 1):
        if not nums[i]:
            continue
        for j in range(i * i, len(arr), i):
            nums[j] = 0

def solve(n):
    check = {n : 1}
    while True:
        tmp = 0
        for i in str(n):
            tmp += int(i) ** 2
        n = tmp

        if n == 1:
            return True
        elif check.get(n):
            return False
        else:
            check[n] = 1

N = int(input())
nums = [1] * 1000001

erathos(nums)

for i in range(2, N + 1):
    if not nums[i]:
        continue

    if solve(i):
        print(i)
