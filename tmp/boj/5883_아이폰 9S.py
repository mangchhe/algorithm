# https://www.acmicpc.net/problem/5883

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def find_length(before, n, idx):
    global ans
    if idx >= len(vol):
        return
    else:
        if vol[idx] == before:
            ans = max(ans, n + 1)
            find_length(vol[idx], n + 1, idx + 1)
        else:
            find_length(vol[idx], 1, idx + 1)

vol_ori = []
vol = []
volDic = {}
ans = 1

for _ in range(int(input())):
    n = int(input())
    vol_ori.append(n)
    volDic[n] = 1

for i in volDic:
    vol = []
    for j in vol_ori:
        if j != i:
            vol.append(j)

    find_length(vol[0], 1, 1)

print(ans)
