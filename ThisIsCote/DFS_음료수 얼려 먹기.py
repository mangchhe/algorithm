"""
    작성일 : 20/09/28
"""

from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):

    if not visited[x][y] and graph[x][y] == '0':
        graph[x][y] = '1'
        visited[x][y] = True
        for i in range(4):
            if x + dx[i] > -1 and x + dx[i] < n and y + dy[i] > -1 and y + dy[i] < m:
                dfs(x + dx[i], y + dy[i])
    else:
        pass

n, m = map(int, input().split())
graph = [list(stdin.readline().rstrip()) for i in range(n)]
visited = [[False] * m for i in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            dfs(i, j)
            result += 1

print(result)