import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def dfs(x, y):

    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if -1 < tx < n and -1 < ty < n:
            if data[tx][ty] == '1':
                data[tx][ty] = '0'
                dfs(tx, ty)


if __name__ == '__main__':

    n = int(input())
    data = []
    res = 0
    for i in range(n):
        data.append(list(input().split()))

    for i in range(n):
        for j in range(n):
            if data[i][j] == '1':
                dfs(i, j)
                res += 1

    print(res)