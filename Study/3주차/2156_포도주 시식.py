import sys

sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [0] * 10001
    for i in range(n):
        data[i] = int(input())
    dp = [0] * 10001
    dp[1] = data[1]
    dp[2] = data[1] + data[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], data[i] + data[i - 1] + dp[i - 3],
                    data[i] + dp[i - 2])

    print(dp[n])