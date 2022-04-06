N = int(input())

squared = [i ** 2 for i in range(1, 317)]
dp = [0]

for i in range(1, N + 1):
    minVal = float('INF')
    for sq in squared:
        if sq > i:
            break
        minVal = min(minVal, dp[i - sq])
    dp.append(minVal + 1)
            
print(dp[N])
