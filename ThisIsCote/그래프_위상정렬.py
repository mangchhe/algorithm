"""
    작성일 : 20/10/30
"""

from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for i in range(v + 1)]
indegree = [0] * (v + 1)
result = []

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topologySort():
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topologySort()

for i in result:
    print(i, end=' ')
