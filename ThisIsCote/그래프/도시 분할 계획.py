"""
    작성일 : 20/10/31
"""

import sys

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n + 1)
edges = []

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = []

for edge in edges:
    c, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result.append(c)

print(sum(result) - max(result))
