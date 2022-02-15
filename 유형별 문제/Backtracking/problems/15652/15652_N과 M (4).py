N, M = map(int, input().split())


def func(n, visited):
    if len(visited) == M:
        print(" ".join(map(str, visited)))
    else:
        for i in range(n, N + 1):
            visited.append(i)
            func(i, visited)
            visited.pop()


func(1, [])
