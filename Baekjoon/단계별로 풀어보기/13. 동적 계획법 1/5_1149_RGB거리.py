'''
dp = []
result = 0

for _ in range(int(input())):
    dp.append(list(map(int, input().split())))

result += min(dp[0])
count = dp[0].index(min(dp[0]))

for i in range(1, len(dp)):

    if count == 0:
        tmp = dp[i][2] if dp[i][1] > dp[i][2] else dp[i][1]
        result += tmp
        count = dp[i].index(tmp)
    elif count == 1:
        tmp = dp[i][2] if dp[i][0] > dp[i][2] else dp[i][0]
        result += tmp
        count = dp[i].index(tmp)
    elif count == 2:
        tmp = dp[i][1] if dp[i][0] > dp[i][1] else dp[i][0]
        result += tmp
        count = dp[i].index(tmp)

print(result)

'''
