import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_parent(parent, a):
    if parent[a] == a:
        return a

    parent[a] = find_parent(parent, parent[a])

    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
arr = [i for i in range(N + 1)]

for _ in range(M):
    op, a, b = map(int, input().split())

    if op:
        print('YES' if find_parent(arr, a) == find_parent(arr, b) else 'NO')
    else:
        union_parent(arr, a, b)
