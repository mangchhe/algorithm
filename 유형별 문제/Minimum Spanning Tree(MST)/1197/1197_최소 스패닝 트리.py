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


V, E = MI()
parent = [i for i in range(V + 1)]
edges = []
for _ in range(E):
    a, b, c = MI()
    edges.append((a, b, c))
ans = 0
cnt = 0

edges.sort(key=lambda x: x[2])

for edge in edges:
    s, e, c = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        ans += c
        cnt += 1
    if cnt == V - 1:
        break

print(ans)
