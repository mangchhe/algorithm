import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':

    N, Q = map(int, input().split())
    data = {}
    for i in range(N + 1):
        data[i] = []
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        data[a].append([b, c])
        data[b].append([a, c])

    for _ in range(Q):
        k, v = map(int, input().split())
        visisted = [0] * (N + 1)
        visisted[v] = 1
        cnt = 0
        q = deque()
        q.extend(data[v])
        while q:
            a, b = q.popleft()
            if visisted[a] == 0:
                if b >= k:
                    cnt += 1
                    visisted[a] = 1
                    q.extend(data[a])

        print(cnt)