import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    dp = [0] * 101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2

    for i in range(5, 101):
        dp[i] = dp[i - 1] + dp[i - 5]

    for i in range(n):
        print(dp[int(input()) - 1])