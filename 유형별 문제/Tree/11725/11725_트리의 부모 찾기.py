from collections import defaultdict

input = __import__("sys").stdin.readline

N = int(input())

visited = [0 for _ in range(N + 1)]
graph = defaultdict(list)
ans = {}

for _ in range(N - 1):

    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

q = [1]
visited[1] = 1

while q:
    now = q.pop()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = 1
            ans[i] = now
            q.append(i)

for i in range(2, N + 1):
    print(ans[i])
