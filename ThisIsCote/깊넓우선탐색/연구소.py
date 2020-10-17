"""
    작성일 : 20/10/17
"""

from collections import deque
from itertools import combinations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().split()))
zero = []
zero_length = 0
two = []
two_length = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '2':
            two.append((i, j))
        elif graph[i][j] == '0':
            zero.append((i, j))

zero_length = len(zero)
two_length = len(two)

def bfs(graph):
    visited = [[False] * m for i in range(n)]
    queue = deque(two)
    count = 0
    remove_two = []

    while queue:
        current = queue.popleft()
        x, y = current[0], current[1]
        if not visited[x][y]:
            visited[x][y] = True
            
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if cx > -1 and cy > -1 and cx < n and cy < m:
                    pass
                else:
                    continue
                if graph[cx][cy] == '0':
                    remove_two.append((cx,cy))
                    graph[cx][cy] = '2'
                    queue.append((cx, cy))
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '0':
                count += 1
    
    for i in remove_two:
        graph[i[0]][i[1]] = '0'

    return count

result = []

for i in list(combinations(zero, 3)):
    a, b, c = i
    graph[a[0]][a[1]] = '1'
    graph[b[0]][b[1]] = '1'
    graph[c[0]][c[1]] = '1'
    result.append(bfs(graph))
    graph[a[0]][a[1]] = '0'
    graph[b[0]][b[1]] = '0'
    graph[c[0]][c[1]] = '0'

print(max(result))