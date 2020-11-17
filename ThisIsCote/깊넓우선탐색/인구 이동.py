"""
    작성일 : 20/11/17
"""

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * n for i in range(n)]
cnt = 0

def bfs(graph, start, visited):

    queue = deque([start])
    visitedRoute = []
    visitedPopularNum = []
    visited[start[0]][start[1]] = True
    nowVisitied = [[False] * n for i in range(n)]
    global cnt
    
    while queue:
        now = queue.popleft()
        nowVisitied[now[0]][now[1]] = True
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if x < n and x > -1 and y < n and y > -1 and not nowVisitied[x][y]:
                if abs(graph[now[0]][now[1]] - graph[x][y]) >= l and abs(graph[now[0]][now[1]] - graph[x][y]) <= r:
                    visitedRoute.append([x, y])
                    visitedPopularNum.append(graph[x][y])
                    visited[x][y] = True
                    nowVisitied[x][y] = True
                    queue.append([x, y])

    if len(visitedRoute):
        visitedRoute.append([start[0], start[1]])
        visitedPopularNum.append(graph[start[0]][start[1]])
        popular = sum(visitedPopularNum) // len(visitedPopularNum)    
        cnt += 1

        for route in visitedRoute:
            graph[route[0]][route[1]] = popular

        del visitedRoute[:]
        del visitedPopularNum[:]
        for i in graph:
            print(i)
        print('---------')


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, [i, j], visited)

print(cnt)