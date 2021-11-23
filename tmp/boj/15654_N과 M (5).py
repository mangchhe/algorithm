def traverse(n, ans):
    if n >= M:
        print(*ans)
        return

    for i in range(N):
        if not visited[arr[i]]:
            visited[arr[i]] = 1
            ans.append(arr[i])
            traverse(n + 1, ans)
            visited[arr[i]] = 0
            ans.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = {i : 0 for i in arr}

traverse(0, [])
