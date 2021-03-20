import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):

    global res

    queue = deque([[x, y]])
    visisted[x][y] = 1
    res += data[x][y]

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 < next_x < n or 0 < next_y < n:
                if visisted[next_x][next_y] == 0:
                    res += data[next_x][next_y]
                    visisted[next_x][next_y] = 1
                    distance[next_x][next_y] = distance[cur_x][cur_y] + 1
                    if distance[next_x][next_y] != n // 2:
                        queue.append([next_x, next_y])


if __name__ == '__main__':

    n = int(input())

    res = 0
    data = []
    visisted = [[0] * (n + 1) for i in range(n + 1)]
    distance = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(n):
        data.append(list(map(int, input().split())))

    bfs(n // 2, n // 2)

    print(res)