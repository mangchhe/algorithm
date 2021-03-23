import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

def dfs(v):

    global res

    if len(idxArr) == m:
        sum = 0
        tmp = []
        for i in idxArr:
            tmp.append(distance[i])
        for i in zip(*tmp):
            sum += min(i)
        res = min(res, sum)
    else:
        for i in range(v, twoLen):
            idxArr.append(i)
            dfs(i + 1)
            idxArr.pop()


if __name__ == '__main__':

    n, m = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(n)]

    distance = []
    one = []
    two = []
    twoLen = 0
    idxArr = []
    res = float('INF')

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                one.append([i, j])
            elif data[i][j] == 2:
                two.append([i, j])
                twoLen += 1

    for i in two:
        tmp = []
        for j in one:
            x, y = i
            xx, yy = j
            tmp.append(abs(x - xx) + abs(y - yy))
        distance.append(tmp)

    dfs(0)

    print(res)