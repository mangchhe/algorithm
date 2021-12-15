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

N, M, K = map(int, input().split())
cities = [i for i in range(N + 1)]
ans = 0
h = []
for i in map(int, input().split()):
    cities[i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    heapq.heappush(h, (w, u, v))

while h:
    w, u, v = heapq.heappop(h)
    
    if find_parent(cities, u) == find_parent(cities, v):
        continue

    union_parent(cities, u, v)
    ans += w

print(ans)
