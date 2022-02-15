# bfs

# from collections import deque

# input = (__import__("sys").stdin.readline

# def solve():

#     q = deque([N])
#     visited[N] = 1
#     distance[N] = 0

#     while q:
#         now = q.popleft()

#         if now == K:
#             break

#         if now * 2 < MAX and not visited[now * 2]:
#             q.appendleft(now * 2)
#             distance[now * 2] = distance[now]
#             visited[now * 2] = 1
#         if now + 1 < MAX and not visited[now + 1]:
#             q.append(now + 1)
#             distance[now + 1] = distance[now] + 1
#             visited[now + 1] = 1
#         if now - 1 > -1 and not visited[now - 1]:
#             q.append(now - 1)
#             distance[now - 1] = distance[now] + 1
#             visited[now - 1] = 1


# N, K = map(int, input().split())
# MAX = 100001
# distance = [0] * MAX
# visited = [0] * MAX

# solve()

# print(distance[K])

# kruskal

import heapq

input = __import__("sys").stdin.readline


def solve():

    q = [(0, N)]
    visited[N] = 1

    while q:
        dist, now = heapq.heappop(q)

        if now == K:
            print(dist)
            break
        if now * 2 < MAX and not visited[now * 2]:
            visited[now * 2] = 1
            heapq.heappush(q, (dist, now * 2))
        if now + 1 < MAX and not visited[now + 1]:
            visited[now + 1] = 1
            heapq.heappush(q, (dist + 1, now + 1))
        if now - 1 > -1 and not visited[now - 1]:
            visited[now - 1] = 1
            heapq.heappush(q, (dist + 1, now - 1))


N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX

solve()
