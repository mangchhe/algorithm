input = __import__('sys').stdin.readline

N = int(input())

rope = []
ans = 0

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(len(rope)):
    ans = max(ans, rope[i] * (i + 1))

print(ans)