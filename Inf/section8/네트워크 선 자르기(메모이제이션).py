import sys

# sys.stdin = open('input.txt', 'rt')


def solve(v):
    if dp[v] != 0:
        return dp[v]
    else:
        dp[v] = solve(v - 1) + solve(v - 2)
        return dp[v]


if __name__ == '__main__':

    n = int(input())

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    print(solve(n))