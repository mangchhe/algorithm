input = __import__("sys").stdin.readline

MI = lambda: map(int, input().split())


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


N, M = MI()
parent = [i for i in range(N + 1)]
pos = []
edges = []
ans = 0
cnt = 0

for i in range(N):
    a, b = MI()
    pos.append((a, b))

for i in range(M):
    a, b = MI()
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1

for i in range(N - 1):
    for j in range(i, N):
        edges.append((((abs(pos[i][0] - pos[j][0]) ** 2 + abs(pos[i][1] - pos[j][1]) ** 2) ** .5), i + 1, j + 1))

edges.sort(key=lambda x: x[0])

for edge in edges:
    c, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        cnt += 1
        ans += c
    if cnt == N - 1:
        break

print('%.2f' % ans)