input = __import__('sys').stdin.readline

N = int(input())
outlines = [list(map(int, input().split())) for _ in range(N)]
outlines.sort()
ans = 0
stack = []

for i in range(N):
    while stack and outlines[i][1] < stack[-1]:
        ans += 1
        stack.pop()

    if stack and outlines[i][1] == stack[-1]:
        continue

    stack.append(outlines[i][1])

print(ans + len(list(filter(lambda x : x > 0, stack))))
