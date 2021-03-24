import sys

# sys.stdin = open('input.txt', 'rt')

if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        maxVal = 0
        for j in range(i - 1, -1, -1):
            if data[i] > data[j] and dp[j] > maxVal:
                maxVal = dp[j]
        dp[i] = maxVal + 1

    print(max(dp))
