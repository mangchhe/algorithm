import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: -x[0])
    dp = [0] * n
    dp[0] = data[0][1]

    for i in range(1, n):
        for j in range(i):
            if data[i][2] < data[j][2]:
                dp[i] = max(dp[i], dp[j] + data[i][1])
        if dp[i] == 0:
            dp[i] = data[i][1]

    print(max(dp))