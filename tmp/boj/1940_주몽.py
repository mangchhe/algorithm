# https://www.acmicpc.net/problem/1940

input = __import__('sys').stdin.readline

N = int(input())
M = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
ans = 0
l, r = 0, len(numbers) - 1

while l < r:
    if numbers[l] + numbers[r] == M:
        ans += 1
        r -= 1
        l += 1
    elif numbers[l] + numbers[r] > M:
        r -= 1
    else:
        l += 1

print(ans)
