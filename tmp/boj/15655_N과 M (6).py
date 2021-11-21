def traverse(n, visited):
    if len(visited) == M:
        print(*visited)
    if n >= N:
        return
    for i in range(n, N):
        visited.append(arr[i])
        traverse(i + 1, visited) 
        visited.pop()


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

traverse(0, [])
