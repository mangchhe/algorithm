import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    dp = [float('INF')] * (m + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(data[i], m + 1):
            dp[j] = min(dp[j - data[i]] + 1, dp[j])

    print(dp[m])