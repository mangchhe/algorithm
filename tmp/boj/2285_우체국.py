# https://www.acmicpc.net/problem/2285

input = __import__('sys').stdin.readline

N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]

l, r = - 10 ** 9, 10 ** 9
ans = 0

while l <= r:
    mid = (l + r) // 2
    lVal, rVal = 0, 0
    for pos, humans in town:
        lVal += abs(mid - 1 - pos) * humans
        rVal += abs(mid - pos) * humans

    if lVal <= rVal:
        r = mid - 1
    else:
        l = mid + 1

print(r)
