import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):

    global res
    if x == maxX and y == maxY:
        res += 1
    else:
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if -1 < cx < n and -1 < cy < n:
                if data[cx][cy] > data[x][y]:
                    dfs(cx, cy)


if __name__ == '__main__':

    n = int(input())
    data = []
    minPos = float('INF')
    minX, minY = 0, 0
    maxPos = 0
    maxX, maxY = 0, 0
    res = 0

    for i in range(n):
        data.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if data[i][j] < minPos:
                minPos = data[i][j]
                minX, minY = i, j
            if data[i][j] > maxPos:
                maxPos = data[i][j]
                maxX, maxY = i, j

    dfs(minX, minY)

    print(res)