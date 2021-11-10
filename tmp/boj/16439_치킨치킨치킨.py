input = __import__('sys').stdin.readline

def traverse(n, arr):
    global ans
    if len(arr) == 3:
        total = 0
        for happy in happiness:
            maxVal = 0
            for j in arr:
                maxVal = max(maxVal, happy[j])
            total += maxVal
        ans = max(ans, total)
    elif n >= M:
        return
    else:
        for i in range(n, M):
            arr.append(i)
            traverse(n + 1, arr)
            arr.pop()


N, M = map(int, input().split())
happiness = [list(map(int, input().split())) for _ in range(N)]
ans = 0

traverse(0, [])

print(ans)
