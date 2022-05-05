import sys
input = sys.stdin.readline

def findParent(a):
    if parent[a] == a:
        return a

    parent[a] = findParent(parent[a])

    return parent[a]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solve():
    while bridges:
        c, a, b = bridges.pop()

        unionParent(a, b)

        a = findParent(S)
        b = findParent(E)

        if a == b:
            print(c)
            exit()

N, M = map(int, input().split())
bridges = []
parent = [i for i in range(0, N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    bridges.append((c, a, b))

bridges.sort(key=lambda x: x[0])

S, E = map(int, input().split())

print(solve())
