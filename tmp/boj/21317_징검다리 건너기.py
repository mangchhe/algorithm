# https://www.acmicpc.net/problem/21317

def traverse(n, e, isK):
    global ans

    if n > N - 1:
        return
    elif n == N - 1:
        ans = min(ans, e)
    else:
        traverse(n + 1, e + energy[n][0], isK)
        traverse(n + 2, e + energy[n][1], isK)
        if not isK:
            traverse(n + 3, e + K, True)

N = int(input())
energy = [tuple(map(int, input().split())) for _ in range(N - 1)]
K = int(input())
ans = float('INF')

traverse(0, 0, False)

print(ans)
