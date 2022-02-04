N, K = map(int, input().split())
stones = list(map(int, input().split()))
dp = [0] * 5001
dp[0] = 1

for i in range(N):
    if not dp[i]:
        continue
    for j in range(i + 1, N):
        p = (j - i) * (1 + abs(stones[i] - stones[j]))
        if p <= K:
            dp[j] = 1

    if dp[N - 1]:
        print('YES')
        exit()

print('NO')
