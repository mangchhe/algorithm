# https://www.acmicpc.net/problem/2108

import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

input = __import__('sys').stdin.readline

N = int(input())
nList = [int(input()) for _ in range(N)]
nList.sort()
nCnt = {}
nSum = 0
flag = True

for i in range(N):
    if not nCnt.get(nList[i]):
        nCnt[nList[i]] = 1
    else:
        nCnt[nList[i]] += 1
    nSum += nList[i]

print(round(nSum / N))

print(nList[N // 2])

maxVal = max(nCnt.values())
tmp = list(filter(lambda x: x[1] == maxVal, nCnt.items()))
if len(tmp) > 1:
    print(tmp[1][0])
else:
    print(tmp[0][0])

print(nList[-1] - nList[0])
