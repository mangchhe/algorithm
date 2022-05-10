def dfs(n, ans):
    if len(ans) == 6:
        print(*ans)
        return

    for i in range(n, N):
        ans.append(nums[i])
        dfs(i + 1, ans)
        ans.pop()


while True:
    N, *nums = list(map(int, input().split()))
    if not N:
        break

    dfs(0, [])
    print()
