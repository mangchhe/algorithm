from collections import defaultdict

input = __import__("sys").stdin.readline
IS = lambda: map(int, input().split())

N, M = IS()

graph = defaultdict(list)
visited = [0] * (N + 1)
res = 0

for _ in range(M):
    a, b = IS()
    graph[b].append(a)

start = int(input())
q = [start]
visited[start] = 1

while q:
    now = q.pop()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
            res += 1

print(res)
