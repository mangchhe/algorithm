input = __import__("sys").stdin.readline


def solve(n, cnt):

    global ans

    if n > B:
        return
    elif n == B:
        ans = min(ans, cnt)
    else:
        solve(n * 10 + 1, cnt + 1)
        solve(n * 2, cnt + 1)


A, B = map(int, input().split())
ans = float("INF")

solve(A, 1)

if ans == float("INF"):
    print(-1)
else:
    print(ans)
