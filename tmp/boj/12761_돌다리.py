from collections import deque

def move(x):
    yield x - 1
    yield x + 1
    yield x + A
    yield x - A
    yield x + B
    yield x - B
    yield x * A
    yield x * B

def solve(x):
    q = deque([(x, 0)])
    arr[x] = 0

    while q:
        x, dist = q.popleft()

        if x == M:
            break
        
        for cx in move(x):
            if cx > -1 and cx < K and arr[cx] > arr[x] + 1:
                arr[cx] = arr[x] + 1
                q.append((cx, arr[cx]))

A, B, N, M = map(int, input().split())
arr = [float('INF')] * 100001
K = 100001

solve(N)

print(arr[M])