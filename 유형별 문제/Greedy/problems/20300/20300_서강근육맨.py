input = __import__("sys").stdin.readline

N = int(input())
loss = list(map(int, input().split()))
loss.sort()

ans = 0

if N == 1:
    ans = loss[-1]
else:
    if N % 2 == 1:
        ans = loss[-1]
        for i in range((len(loss) - 1) // 2):
            ans = max(ans, loss[i] + loss[-i - 2])
    else:
        for i in range(len(loss) // 2):
            ans = max(ans, loss[i] + loss[-i - 1])

print(ans)
