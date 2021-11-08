N, A, D = map(int, input().split())

ans = 0
target = A

for i in map(int, input().split()):
    if target == i:
        ans += 1
        target += D

print(ans)
