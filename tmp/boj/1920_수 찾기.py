# https://www.acmicpc.net/problem/1920

N = int(input())
nList = list(map(int, input().split()))
nDic = {}
for n in nList:
    nDic[n] = 1
M = int(input())

for i in list(map(int, input().split())):
    if nDic.get(i):
        print(1)
    else:
        print(0)
