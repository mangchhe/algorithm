input = __import__('sys').stdin.readline

N = int(input())
M = int(input())
''' 방법1
vip가 있다면 i, i + 1 까지 i - 1 데이터 삽입
'''
# vips = [0] * (N + 1)
# dp = [0] * (N + 2)
# dp[0], dp[1]= 1, 1

# for _ in range(M): vips[int(input())] = 1

# if vips[1]:
#     i = 3
#     dp[2] = 1
# else:
#     i = 2
# while i <= N:
#     if vips[i]:
#         dp[i], dp[i + 1] = dp[i - 1], dp[i - 1]
#     else:
#         if not dp[i]:
#             dp[i] = dp[i - 1] + dp[i - 2]
#     i += 1

# print(dp[N])

''' 방법2
vip 기준으로 각 경우의 수 곱셈
'''
dp = [1, 1]
ans = 1

for i in range(2, 41):
    dp.append(dp[-1] + dp[-2])

tmp = 0
for _ in range(M):
    vip = int(input())
    ans *= dp[vip - tmp - 1]
    tmp = vip

print(ans * dp[N - tmp])
