input = __import__("sys").stdin.readline


def func(x, y, c):

    global ans

    if y > 9:
        ans = min(ans, c)
    elif x > 9:
        func(0, y + 1, c)
    elif paper[x][y] == 1:
        for k in range(5):
            if x + k > 9 and y + k > 9:
                continue

            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if paper[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        paper[i][j] = 0

                func(x + k + 1, y, c + 1)

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        paper[i][j] = 1
    else:
        func(x + 1, y, c)


paper = [list(map(int, input().split())) for _ in range(10)]
ans = float("INF")

func(0, 0, 0)

print(ans) if ans != float("INF") else print(-1)
