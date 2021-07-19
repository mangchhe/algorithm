from collections import defaultdict

input = __import__('sys').stdin.readline

MI = lambda: map(int, input().split())

def bfs():

    q = [X]
    visited[X] = 1
    distance = 1

    while q:
        tmp = []
        for i in q:
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = 1
                    if distance == K:
                        ans.append(j)
                    else:
                        tmp.append(j)
        q = tmp
        distance += 1

N, M, K, X = MI()

visited = [0] * (N + 1)
graph = defaultdict(list)
ans = []

for _ in range(M):
    s, e = MI()
    graph[s].append(e)

bfs()

if ans:
    for i in sorted(ans):
        print(i)
else:
    print(-1)