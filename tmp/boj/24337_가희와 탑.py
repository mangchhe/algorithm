N, a, b = map(int, input().split())
ans = [1 for i in range(N)]

if N < a + b - 1:
    print(-1)
    exit()

top = N - b

if a != 1:
    ans[top] = max(a, b)
else:
    ans[0] = max(a, b)

now = top + 1
height = b - 1
while height > 1:
    ans[now] = height
    height -= 1
    now += 1

now = top - 1
height = a - 1
while height > 1:
    ans[now] = height
    height -= 1
    now -= 1

print(*ans)
