# https://www.acmicpc.net/problem/1916

from collections import defaultdict
import heapq

input = __import__('sys').stdin.readline

def solve(start):
    q = [(0, start)]
    heapq.heapify(q)
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in route[now]:
            if dis + i[1] < distance[i[0]]:
                distance[i[0]] = dis + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))

N = int(input())
M = int(input())

distance = [float('INF')] * (N + 1)
route = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    route[a].append((b, c))

A, B = map(int, input().split())

solve(A)

print(distance[B])
