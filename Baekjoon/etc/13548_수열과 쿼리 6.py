'''
작성일 : 7/29
'''
from sys import stdin

N = int(stdin.readline())
NList = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
MList = []
for i in range(M):
    MList.append(list(map(int, stdin.readline().split())))

for i in range(M):
    
    tmp = NList[MList[i][0] - 1:MList[i][1] + 1]

    tmpDic = {}

    for j in tmp:

        if j not in tmpDic:

            tmpDic[j] = 1

        else:

            tmpDic[j] += 1

    print(max(tmpDic.values()))

