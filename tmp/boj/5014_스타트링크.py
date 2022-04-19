from collections import deque

def bfs(start):    
    visited[S] = 0
    s = deque([start])

    while s:
        now = s.popleft()

        if now == G:
            return visited[G]

        if U and now + U < F + 1 and visited[now + U] == -1:
            visited[now + U] = visited[now] + 1
            s.append(now + U)

        if D and now - D > 0 and visited[now - D] == -1:
            visited[now - D] = visited[now] + 1
            s.append(now - D)

    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)

print(bfs(S))
