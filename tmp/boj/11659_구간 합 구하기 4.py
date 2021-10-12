# https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nList = list(map(int, input().split()))
sumList = [0]

for i in range(1, len(nList) + 1):
    sumList.append(sumList[i - 1] + nList[i - 1])

for _ in range(M):
    s, e = map(int, input().split())
    s = s - 1
    print(sumList[e] - sumList[s])
