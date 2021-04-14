import sys

input = sys.stdin.readline

if __name__ == '__main__':

    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (K + 1)

    for w, k in data:
        for i in range(K, w - 1, -1):
            dp[i] = max(dp[i - w] + k, dp[i])

    print(max(dp))