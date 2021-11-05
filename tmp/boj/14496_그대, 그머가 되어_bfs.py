from collections import defaultdict, deque

input = __import__('sys').stdin.readline

def bfs(start, target):
    q = deque([(start, 0)])
    visited[start] = 1

    while q:
        now, dist = q.popleft()
        if now == target:
            return dist
        for i in mov[now]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, dist + 1))
    
    return -1

A, B = map(int, input().split())
N, M = map(int, input().split())
visited = [0] * (N + 1)
ans = -1
mov = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    mov[b].append(a)
    mov[a].append(b)

print(bfs(B, A))
