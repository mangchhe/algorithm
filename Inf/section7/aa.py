import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')


def bfs(v):

    queue = deque([v])
    visited[v] = 1

    while queue:
        now = queue.popleft()
        if now == e:
            return
        else:
            for d in (now - 1, now + 1, now + 5):
                if d < 1 or d > 10000:
                    continue
                if visited[d] == 0:
                    queue.append(d)
                    visited[d] = 1
                    distance[d] = distance[now] + 1


if __name__ == '__main__':

    s, e = map(int, input().split())

    visited = [0] * 10001
    distance = [0] * 10001

    bfs(s)

    print(distance[e])