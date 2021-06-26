## 크루스칼(Kruskal) 알고리즘

- 모든 노드를 최소 비용으로 연결시키는 것을 목적으로 한다.
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
