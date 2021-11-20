def traverse(n, visited):
    if len(visited) == M:
        print(*visited)
        return

    if n >= M:
        return
    
    visited.append(arr[n])
    traverse(n, visited)
    visited.pop()
    traverse(n + 1, visited)

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

traverse(0, [])
