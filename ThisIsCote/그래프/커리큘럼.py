"""
    작성일 : 20/10/31
"""

import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())

indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    result = copy.deepcopy(time)
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topologySort():
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            time[i] = max(time[i], result[i] + time[now])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in time:
        print(i)

topologySort()