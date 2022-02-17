# Minimum Spanning Tree (MST)

- 모든 노드를 최소 비용으로 연결하는 것을 목적으로 한다.

## 크루스칼(Kruskal) 알고리즘

- 간선을 비용을 기준으로 오름차순으로 정렬한 뒤에 하나씩 꺼내며 노드를 연결
- 노드 연결 시 사이클이 존재하는지 확인을 하며 N-1개 간선이 연결될 때까지 진행한다. (모든 노드가 이어질 때까지)
- 간선 수가 적을 때 프림 알고리즘보다 유리
- O(ElogE) 라는 시간 복잡도를 가진다.

### 대표 소스

``` python
import heapq
from sys import stdin

input = stdin.readline

def find_parent(parent, a):
    if parent[a] == a:
        return parent[a]

    parent[a] = find_parent(parent, parent[a])

    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())

graph = []
parent = [i for i in range(n + 1)]
cnt = 0
res = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))

while graph:
    c, s, e = heapq.heappop(graph)
    if find_parent(parent, s) == find_parent(parent, e):
        pass
    else:
        union_parent(parent, s, e)
        cnt += 1
        res += c
        if cnt == n - 1:
            break

print(res)
```

## 프림 알고리즘 (Prim's Algorithm)

- 시작 지점을 정하고 각 노드에서의 최소 비용의 간선을 따라가며 모두 이어질 때까지 진행하는 알고리즘
- 간선 수가 많을 때 크루스칼 알고리즘보다 유리
- O(ElogV)

### 대표 소스

``` python
import sys
import heapq
input = sys.stdin.readline

def prim(start):
    global totalCost
    h = graph[start]
    heapq.heapify(h)
    visited[start] = 1
    
    while h:
        c, s, e = heapq.heappop(h)
        if visited[e]:
            continue
        visited[e] = 1
        totalCost += c
        
        for node in graph[e]:
            if not visited[node[2]]:
                heapq.heappush(h, node)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
totalCost = 0

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([c, s, e])
    graph[e].append([c, e, s])

prim(1)

print(totalCost)
```
