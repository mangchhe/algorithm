"""
    작성일 : 20/10/30
"""

import sys
input = sys.stdin.readline

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

v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0

for edge in edges:
    c, a, b = edge
    #if parent[a] != parent[b]:
    if findParent(parent, a) != findParent(parent, b):
        result += c
        unionParent(parent, a, b)

print(parent)
print(result)