from collections import defaultdict

input = __import__("sys").stdin.readline


def solve():
    q = []
    seq = 1

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        tmp = []
        for i in q:
            res[i] = seq
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    tmp.append(j)
        q = tmp
        seq += 1


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)
res = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

solve()

print(" ".join(map(str, res[1:])))
