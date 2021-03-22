import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):

    global cnt

    queue = deque([[x, y]])

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            tx, ty = cx + dx[i], cy + dy[i]
            if -1 < tx < n and -1 < ty < n:
                if data[tx][ty] == '1':
                    data[tx][ty] = '0'
                    queue.append([tx, ty])
                    cnt += 1


if __name__ == '__main__':

    n = int(input())
    res = 0
    resArr = []
    data = []
    for i in range(n):
        data.append(list(input()))

    for i in range(n):
        for j in range(n):
            if data[i][j] == '1':
                cnt = 1
                data[i][j] = '0'
                dfs(i, j)
                resArr.append(cnt)
                res += 1

    print(res)
    for r in sorted(resArr):
        print(r)