"""
    작성일 : 20/09/28
"""

from sys import stdin
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, start):

    queue = deque([[start[0], start[1]]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx > -1 and tx < n and ty > -1 and ty < m:
                if graph[tx][ty] == 1:
                    graph[tx][ty] = graph[x][y] + 1
                    queue.append([tx,ty])
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = [list(map(int, stdin.readline().rstrip())) for i in range(n)]

print(bfs(graph, (0, 0)))
