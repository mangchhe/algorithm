input = __import__('sys').stdin.readline

N, D = map(int, input().split())
shortcut = {}
dp = [D] * (D + 1)
dp[0] = 0

for _ in range(N):
    s, e, d = map(int, input().split())
    if not shortcut.get(s):
        shortcut[s] = [(e, d)]
    else:
        shortcut[s].append((e, d))

for s in range(D):
    if shortcut.get(s):
        for e, d in shortcut.get(s):
            if e <= D:
                dp[e] = min(dp[s] + d, dp[e])
    dp[s + 1] = min(dp[s] + 1, dp[s + 1])

print(dp[D])
