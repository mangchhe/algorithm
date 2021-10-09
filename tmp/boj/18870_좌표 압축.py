# https://www.acmicpc.net/problem/18870

N = int(input())
nList = list(map(int, input().split()))
nDic = {}

for idx, i in enumerate(sorted(set(nList))):
    if not nDic.get(i):
        nDic[i] = idx

for i in nList:
    print(nDic[i], end = ' ')
