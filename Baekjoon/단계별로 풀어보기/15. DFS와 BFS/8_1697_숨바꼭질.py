from collections import deque

N, K = map(int, input().split())

NList = {}

def solve(start_node):

    visited = [0] * 100001
    start_node = deque([start_node])
    count = 0

    while True:

        tmp = []

        while start_node:

            current_node = start_node.popleft()

            if current_node == K:

                return count

            if not visited[current_node]:

                visited[current_node] = 1
                create(current_node, tmp)

        start_node.extend(tmp)
        count += 1


def create(N, tmp):

    NList[N] = []
    if N - 1 >= 0:
        tmp.append(N-1)
        NList[N].append(N - 1)
    if N + 1 < 100001:
        tmp.append(N+1)
        NList[N].append(N + 1)
    if N * 2 < 100001:
        tmp.append(N*2)
        NList[N].append(N * 2)

print(solve(N))