import sys

sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [0] * 300
    for i in range(n):
        data[i] = int(input())
    dp = [0] * 300
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(data[0] + data[2], data[1] + data[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + data[i] + data[i - 1], dp[i - 2] + data[i])

    print(dp[n - 1])
