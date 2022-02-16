import sys
import heapq

input = __import__('sys').stdin.readline

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def sameParent(parent, a, b):
    if findParent(parent, a) == findParent(parent, b):
        return 1
    else:
        return 0

def findParent(parent, a):
    if parent[a] == a:
        return a
    
    parent[a] = findParent(parent, parent[a])

    return parent[a]

N, P = map(int, input().split())
countryCost = [0] + [int(input()) for _ in range(N)]
h = []
parent = [i for i in range(N + 1)]

for _ in range(P):
    s, e, l = map(int, input().split())
    heapq.heappush(h, (l * 2 + countryCost[s] + countryCost[e], s, e))

cnt = 0
cost = 0
while h:
    l, s, e = heapq.heappop(h)

    if not sameParent(parent, s, e):
        unionParent(parent, s, e)
        cnt += 1
        cost += l
        if cnt == N - 1:
            break

print(cost + min(countryCost[1:]))
