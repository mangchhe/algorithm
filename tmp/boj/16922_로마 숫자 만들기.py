N = int(input())
arr = [1, 5, 10, 50]
ans = {}

def traverse(idx, n, cnt):
    if cnt == N:
        ans[n] = 1
        return
    if cnt > N or idx > 3:
        return

    for i in range(N + 1 - cnt):
        traverse(idx + 1, n + arr[idx] * i, cnt + i)

traverse(0, 0, 0)

print(len(ans))
