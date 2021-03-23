import sys

# sys.stdin = open('input.txt', 'rt')

def solve(v):

    if v < 3:
        return dp[v]
    else:
        if dp[v] != 0:
            return dp[v]
        else:
            return solve(v - 1) + solve(v - 2)


if __name__ == '__main__':

    dp = [0] * 46
    dp[1] = 1
    dp[2] = 2

    n = int(input())

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])