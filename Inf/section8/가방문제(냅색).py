import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n, w = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0] * (w + 1)

    for i in range(n):
        for j in range(data[i][0], w + 1):
            dp[j] = max(dp[j - data[i][0]] + data[i][1], dp[j])

    print(max(dp))
