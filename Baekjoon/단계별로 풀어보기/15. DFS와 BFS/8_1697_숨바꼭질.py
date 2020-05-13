from collections import deque

N, K = map(int, input().split())

NList = {}

def solve(start_node):

    visited = [0] * 100001
    start_node = deque([start_node])

    while start_node:

        current_node = start_node.popleft()
        create(current_node)

        if not visited[current_node]:

            visited[current_node] = 1
            start_node.extend(NList[current_node])

            if current_node == K:

                length = visited.count(1)

                for i in range(length):

                    if 3**i > length:

                        return i


def create(N):

    NList[N] = []
    if N - 1 >= 0:
        NList[N].append(N - 1)
    if N + 1 < 100001:
        NList[N].append(N + 1)
    if N * 2 < 100001:
        NList[N].append(N * 2)

print(solve(N))