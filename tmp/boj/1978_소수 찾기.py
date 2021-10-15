# https://www.acmicpc.net/problem/1978

N = int(input())
nList = list(map(int, input().split()))

isDecimals = [False, False] + [True] * 999

for i in range(2, int(1001 ** .5) + 1):
    if isDecimals[i]:
        for j in range(i + i, 1001, i):
            isDecimals[j] = False

print(len(list(filter(lambda x: isDecimals[x], nList))))
