import sys

# sys.stdin = open('input.txt', 'rt')

cntDic = {}

for d in list(input()):
    if d not in cntDic:
        cntDic[d] = 1
    else:
        cntDic[d] += 1

for d in list(input()):
    if d not in cntDic:
        cntDic[d] = 1
    else:
        cntDic[d] -= 1
        if cntDic[d] == 0:
            del cntDic[d]

if not cntDic:
    print('YES')
else:
    print('NO')