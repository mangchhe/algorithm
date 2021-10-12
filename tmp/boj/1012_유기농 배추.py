# https://www.acmicpc.net/problem/1012

from collections import deque

input = __import__('sys').stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(arr, visited, x, y):
    ans = 0
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if -1 < cx < len(arr) and -1 < cy < len(arr[0]) and not visited[cx][cy]:
                visited[cx][cy] = 1
                if arr[cx][cy] == 1:
                    q.append((cx, cy))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and farm[i][j] == 1:
                bfs(farm, visited, i, j)
                ans += 1
    print(ans)
