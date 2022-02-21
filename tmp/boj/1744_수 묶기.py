input = __import__('sys').stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
plus = list(filter(lambda x : x > 0, arr))
minus = list(filter(lambda x: x < 1, arr))
plus.sort(reverse=True)
minus.sort()
ans = 0

for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        ans += plus[i] 
    elif plus[i] != 1 and plus[i + 1] != 1:
        ans += plus[i] * plus[i + 1]
    else:
        ans += plus[i] + plus[i + 1]

for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        ans += minus[i]
    else:
        ans += minus[i] * minus[i + 1]

print(ans)
