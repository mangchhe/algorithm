def traverse(n, visited):
    if len(visited) == M:
        print(*visited)
        return
    if n >= N:
        return
    
    for i in range(N):
        visited.append(arr[i])
        traverse(i, visited)
        visited.pop()


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

traverse(0, [])
