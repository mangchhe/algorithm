import heapq

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

N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
h = []
parent = [i for i in range(N)]
ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        heapq.heappush(h, ((abs(arr[i][0] - arr[j][0]) ** 2 + abs(arr[i][1] - arr[j][1]) ** 2) ** .5, i, j))

while h:
     dist, a, b = heapq.heappop(h)
     if find_parent(parent, a) == find_parent(parent, b):
         continue
     union_parent(parent, a, b)
     ans += dist
     if parent.count(parent[a]) == N:
         break

print('%.2f' % ans)
