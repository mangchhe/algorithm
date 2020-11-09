"""
    작성일 : 20/11/09 - 런타임 에러
"""

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
s, x, y = map(int, input().split())

queue = deque([])
graphDic = {}

for i in range(n):
    for j in range(n):
        if graph[i][j] in graphDic:
            graphDic[graph[i][j]].append((i, j))
        else:
            graphDic[graph[i][j]] = [(i, j)]

for i in range(1, k + 1):
    queue.extend(graphDic[i])

cnt = 0

while True:
    if cnt == s:
        break
    nowVal = 0
    tmp = []
    for i in queue:
        nowVal = graph[i[0]][i[1]]
        for j in range(4):
            x = i[0] + dx[j]
            y = i[1] + dy[j]
            if x < n and x > -1 and y < n and y > -1:
                if graph[x][y] == 0:
                    graph[x][y] = nowVal
                    tmp.append((x, y))
            else:
                pass
    cnt += 1
    queue.extend(tmp)

print(graph[x-1][y-1])
