# https://www.acmicpc.net/problem/20551

input = __import__('sys').stdin.readline

N, M = map(int, input().split())
nPos = {}
nList = sorted([int(input()) for _ in range(N)])
for idx, i in enumerate(nList):
    if nPos.get(i) == None:
        nPos[i] = idx

for _ in range(M):
    n = int(input())
    if nPos.get(n) == None:
        print(-1)
    else:
        print(nPos[n])
