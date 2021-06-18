input = __import__("sys").stdin.readline
MI = lambda: map(int, input().split())

N, M = MI()
# 방법 1

# visits = list(MI())
# s = 0
# e = 1
# sum = visits[s]
# maxVal = 0
# cnt = 0

# while s < e:
#     if e - s == M:
#         if sum > maxVal:
#             maxVal = sum
#             cnt = 1
#         elif sum == maxVal:
#             cnt += 1
#     if e - s < M and e < N:
#         sum += visits[e]
#         e += 1
#     else:
#         sum -= visits[s]
#         s += 1

# if maxVal != 0:
#     print(maxVal)
#     print(cnt)
# else:
#     print("SAD")

# 방법 2

visits = [0] + list(MI())
res = [0, 0]
s = sum(visits[:M])
for i in range(M, N + 1):
    s += visits[i]
    s -= visits[i - M]
    if s > res[0]:
        res = [s, 1]
    elif s == res[0]:
        res[1] += 1

if res[0] == 0:
    print("SAD")
else:
    print(*res)
