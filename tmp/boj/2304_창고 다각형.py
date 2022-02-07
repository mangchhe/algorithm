input = __import__('sys').stdin.readline

N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]
ans = 0

pillar.sort()

stack = []
for x, h in pillar:
    if stack and stack[0][1] <= h:
        ans += (x - stack[0][0]) * stack[0][1]
        stack = [(x, h)]
    else:
        stack.append((x, h))

stack = []
for x, h in reversed(pillar):
    if stack and stack[0][1] < h:
        ans += (stack[0][0] - x) * stack[0][1]
        stack = [(x, h)]
    else:
        stack.append((x, h))

ans += stack[0][1]

print(ans)
