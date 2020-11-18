"""
    작성일 : 20/11/09 - 런타임 에러
    수정일 : 20/11/18
    
    url : https://www.acmicpc.net/problem/18405
"""

from collections import deque
import sys

input = sys.stdin.readline

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
    if i in graphDic:
        queue.extend(graphDic[i])

for _ in range(s):
    nowVal = 0
    tmp = []
    while queue: # for i in queue -> 실수 queue의 값이 사라지지 않고 계속 쌓여서 시간 초과
        i = queue.popleft()
        nowVal = graph[i[0]][i[1]]
        for j in range(4):
            tx = i[0] + dx[j]
            ty = i[1] + dy[j]
            if tx < n and tx > -1 and ty < n and ty > -1:
                if graph[tx][ty] == 0:
                    graph[tx][ty] = nowVal
                    tmp.append((tx, ty))
            else:
                pass

    queue.extend(tmp)
        
print(graph[x-1][y-1])
