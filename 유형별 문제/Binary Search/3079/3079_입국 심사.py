input = __import__("sys").stdin.readline

N, M = map(int, input().split())
K = [int(input()) for _ in range(N)]
K = sorted(K)

start = 1
end = K[-1] * M

while start < end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(N):
        cnt += mid // K[i]

    if cnt < M:
        start = mid + 1
    else:
        end = mid

print(end)
