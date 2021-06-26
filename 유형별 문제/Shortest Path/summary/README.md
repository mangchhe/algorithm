## 다익스트라(Dijkstra) 알고리즘

- 특정한 한 노드에서 다른 모든 노드까지 가는데 걸리는 최단 경로를 찾는 알고리즘이다.
- O(ElogV) 라는 시간 복잡도를 가진다.

### 대표 소스

``` python
import heapq
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
distance = [float('INF')] * (N + 1)
graph = [[] for _ in range(N + 1)]
start = int(input())

def dijkstra(start):

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

if __name__ == '__main__':

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(start)

    for i in range(1, N + 1):
        print(distance[i])
```

## 플로이드 워셜(Floyd-Warshall) 알고리즘

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산하는 알고리즘이다.
- O(N^3) 라는 시간 복잡도를 가진다.

### 대표 소스

``` python
N = int(input())
M = int(input())
graph = [[float('INF')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print("%5s" % (graph[i][j]), end="")
    print()
```
