input = __import__("sys").stdin.readline
N = int(input())
zum = [list(map(int, input().split())) for _ in range(N)]
visisted = [0] * N
ans = float("INF")


def func(n, cnt):
    global ans
    if N // 2 == cnt:
        sum1 = 0
        sum2 = 0
        for i in range(N):
            for j in range(i + 1, N):
                if not visisted[i] and not visisted[j]:
                    sum1 += zum[i][j]
                    sum1 += zum[j][i]
                elif visisted[i] and visisted[j]:
                    sum2 += zum[i][j]
                    sum2 += zum[j][i]
        ans = min(ans, abs(sum1 - sum2))

    else:
        for i in range(n, N):
            if not visisted[i]:
                visisted[i] = 1
                func(i, cnt + 1)
                visisted[i] = 0


func(0, 0)

print(ans)
