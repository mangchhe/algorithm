input = __import__("sys").stdin.readline

N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]
ans = 0

for i in range(len(money) - 1, -1, -1):
    ans += K // money[i]
    K %= money[i]

print(ans)
