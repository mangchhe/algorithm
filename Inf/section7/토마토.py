import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():

    global zeroCnt

    x, y = 0, 0

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            tx, ty = cx + dx[i], cy + dy[i]
            if -1 < tx < n and -1 < ty < m:
                if data[tx][ty] == 0:
                    distance[tx][ty] = distance[cx][cy] + 1
                    data[tx][ty] = 1
                    queue.append([tx, ty])
                    zeroCnt -= 1
                    x, y = tx, ty

    return distance[x][y]


if __name__ == '__main__':

    m, n = map(int, input().split())

    data = [list(map(int, input().split())) for i in range(n)]

    res = 0
    zeroCnt = 0
    distance = [[0] * m for i in range(n)]
    queue = deque([])

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                zeroCnt += 1
            elif data[i][j] == 1:
                queue.append([i, j])
                data[i][j] = 1

    res = bfs()

    if zeroCnt == 0:
        print(res)
    else:
        print(-1)