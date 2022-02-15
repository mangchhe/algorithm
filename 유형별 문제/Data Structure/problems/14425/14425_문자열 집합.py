input = __import__("sys").stdin.readline

N, M = map(int, input().split())

texts = {}
ans = 0

for _ in range(N):
    texts[input().rstrip()] = 1

for _ in range(M):
    if input().rstrip() in texts:
        ans += 1

print(ans)
