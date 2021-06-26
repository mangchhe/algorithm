input = __import__("sys").stdin.readline

N = int(input())

nList = list(map(int, input().rstrip().split()))
stack = []
ans = []

for i in range(len(nList)):
    while stack:
        if stack[-1][1] >= nList[i]:
            ans.append(stack[-1][0] + 1)
            stack.append((i, nList[i]))
            break
        else:
            stack.pop()

    if not stack:
        stack.append((i, nList[i]))
        ans.append(0)

print(" ".join(map(str, ans)))
