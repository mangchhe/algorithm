# https://www.acmicpc.net/problem/21275

input = __import__('sys').stdin.readline

A, B = input().split()
aMax, bMax = 2, 2
nList = {}
ans = []
ansCnt = 0

def notation_converter(n, c):
    res = 0
    idx = 0
    for i in n[::-1]:
        res += nList[i] * (c ** idx)
        idx += 1
    return res

for i in range(36):
    if i < 10:
        nList[str(i)] = i
    else:
        nList[chr(i + 87)] = i

for i in A:
    aMax = max(aMax, nList[i])
for i in B:
    bMax = max(bMax, nList[i])

for i in range(aMax + 1, 37):
    for j in range(bMax + 1, 37):
        if i == j:
            continue
        nA = notation_converter(A, i)
        nB = notation_converter(B, j)
        if nA == nB and nA < 2 ** 63 and nB < 2 ** 63:
            ansCnt += 1
            ans.append((nA, i, j))
    if ansCnt > 1:
        break

if ansCnt == 0:
    print('Impossible')
elif ansCnt > 1:
    print('Multiple')
elif ansCnt == 1:
    for i in ans[0]:
        print(i, end=" ")
