import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1]
dy = [-1, 1, 0]


def dfs(x, y):

    global res

    if x == 0:
        res = y
    else:
        for i in range(3):
            tx, ty = x + dx[i], y + dy[i]
            if -1 < tx < n and -1 < ty < n:
                if data[tx][ty] == 1:
                    data[tx][ty] = 2
                    dfs(tx, ty)
                    break


if __name__ == '__main__':

    n = 10
    res = 0

    data = [list(map(int, input().split())) for _ in range(10)]

    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                dfs(i, j)
                break

    print(res)