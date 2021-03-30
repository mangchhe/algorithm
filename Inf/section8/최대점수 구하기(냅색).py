import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n, m = map(int, input().split())
    dp = [0] * (m + 1)

    for _ in range(n):
        z, t = map(int, input().split())
        for i in range(m, t - 1, -1):
            dp[i] = max(dp[i - t] + z, dp[i])

    print(max(dp))