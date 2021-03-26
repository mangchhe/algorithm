import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        for j in range(i):
            if dp[i] <= dp[j]:
                for k in range(n):
                    if data[k] == i + 1:
                        if dp[i] == 0:
                            dp[i] = 1
                        break
                    if data[k] == j + 1:
                        dp[i] = dp[j] + 1

    print(max(dp))