from collections import defaultdict
import heapq

input = __import__("sys").stdin.readline


def solve():

    h = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(h, i)

    while h:
        now = heapq.heappop(h)
        print(now, end=" ")
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(h, i)


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

solve()
