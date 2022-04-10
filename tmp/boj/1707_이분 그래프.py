import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    
    visited[start] = 1

    while q:
        now = q.popleft()
        partition = visited[now]

        for i in graph[now]:
            if visited[i]:
                if partition == visited[i]:
                    return 0
            else:
                visited[i] = 2 if partition == 1 else 1
                q.append(i)
    
    return 1


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (v + 1)
    
    for i in range(1, v + 1):
        if not visited[i] and not bfs(i):
            print('NO')
            break
    else:
        print('YES')
