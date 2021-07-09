input = __import__("sys").stdin.readline

N = int(input())
amount = list(map(int, input().split()))
amount.sort()
ans = amount[-1]

for i in range(len(amount) - 1):
    ans += amount[i] / 2

print(ans)
