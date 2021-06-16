N, M = map(int, input().split())


def func(n, visited):
    if len(visited) == M:
        print(" ".join(map(str, visited)))
    else:
        for i in range(n, N + 1):
            if i not in visited:
                visited.append(i)
                func(i + 1, visited)
                visited.pop()


func(1, [])
