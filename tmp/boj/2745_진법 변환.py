# https://www.acmicpc.net/problem/2745

input = __import__('sys').stdin.readline


N, B = input().split()
B = int(B)
ans = 0

idx = 0
for i in N[::-1]:
    if i.isdigit():
        ans += int(i) * (B ** idx)
    else:
        ans += (ord(i) - 55) * (B ** idx)
    idx += 1

print(ans)
