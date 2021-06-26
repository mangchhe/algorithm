T = int(input())

dp = {}

def factorial(n):

    if n in dp:
        return dp[n]
    elif n < 2:
        return 1
    else:
        dp[n] = n * factorial(n - 1)
        return dp[n]

def conbi(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))

for _ in range(T):
    N, M = map(int, input().split())

    print(conbi(M, N))