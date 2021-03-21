import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):

    queue = deque([[x, y]])
    visisted[x][y] = 1

    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == n - 1 and cur_y == n - 1:
            break
        for i in range(4):
            nxt_x = cur_x + dx[i]
            nxt_y = cur_y + dy[i]
            if -1 < nxt_x < n and -1 < nxt_y < n:
                if visisted[nxt_x][nxt_y] == 0 and road[nxt_x][nxt_y] == '0':
                    visisted[nxt_x][nxt_y] = 1
                    queue.append([nxt_x, nxt_y])
                    distance[nxt_x][nxt_y] = distance[cur_x][cur_y] + 1


if __name__ == '__main__':

    n = 7
    road = []
    visisted = [[0] * n for i in range(n)]
    distance = [[0] * n for i in range(n)]

    for i in range(n):
        road.append(list(input().split()))

    bfs(0, 0)

    if distance[n - 1][n - 1] == 0:
        print(-1)
    else:
        print(distance[n - 1][n - 1])
