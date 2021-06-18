from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
cnt = 0
totalCost = 0
res = 0
distance = []
for _ in range(M):
    a, b, c = map(int, input().split())
    distance.append((a, b, c))
    totalCost += c
distance.sort(key=lambda x: -x[2])


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


while distance:
    a, b, c = distance.pop()
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        res += c
        cnt += 1
        if cnt == N - 1:
            break

if cnt == N - 1:
    print(totalCost - res)
else:
    print(-1)
