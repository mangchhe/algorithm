input = __import__("sys").stdin.readline

N = int(input())
time = list(map(int, input().split()))
delay = 0
ans = 0

time.sort()

for t in time:
    ans += t + delay
    delay += t

print(ans)
