input = __import__("sys").stdin.readline

cost = []

N = int(input())
ans = 0

for _ in range(N):
    cost.append(int(input()))

cost.sort(reverse=True)

for i, c in enumerate(cost, start=1):
    if i % 3 != 0:
        ans += c

print(ans)
