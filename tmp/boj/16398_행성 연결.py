import heapq
input = __import__('sys').stdin.readline

def find_parent(parent, a):
    if parent[a] == a:
        return a
    
    parent[a] = find_parent(parent, parent[a])

    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def sameParent(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return 1
    return 0

N = int(input())
h = []
parent = [i for i in range(N)]
cnt = 1
ans = 0

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1):
    for j in range(1 + i, N):
        heapq.heappush(h, (graph[i][j], i, j))

while h:
    cost, x, y = heapq.heappop(h)

    if not sameParent(parent, x, y):
        union_parent(parent, x, y)
        ans += cost
        cnt += 1
        if cnt == N:
            break

print(ans)
