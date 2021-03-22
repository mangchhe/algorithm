import sys
from collections import deque
import copy

sys.setrecursionlimit(10 ** 6)

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, k):

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if -1 < tx < n and -1 < ty < n:
            if tmp[tx][ty] > k:
                tmp[tx][ty] = 0
                dfs(tx, ty, k)


if __name__ == '__main__':

    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for k in range(1, 101):
        tmp = copy.deepcopy(data)
        sum = 0
        for i in range(n):
            for j in range(n):
                if tmp[i][j] > k:
                    dfs(i, j, k)
                    sum += 1
        if sum == 0:
            break
        res = max(res, sum)

    print(res)