from functools import reduce

board = [list(map(int, input().split())) for _ in range(9)]
zeroCnt = list(reduce(lambda x, y: x + y, board)).count(0)
cnt = 0


def judge(x, y, n):
    for i in range((x // 3) * 3, (x // 3 + 1) * 3):
        for j in range((y // 3) * 3, (y // 3 + 1) * 3):
            if board[i][j] == n:
                return False
    for i in range(9):
        if board[x][i] == n or board[i][y] == n:
            return False

    return True


def func(x, y):
    global cnt
    if x >= 9:
        if cnt == zeroCnt:
            for i in board:
                print(" ".join(map(str, i)))
            exit()
    if board[x][y] == 0:
        for i in range(1, 10):
            if judge(x, y, i):
                board[x][y] = i
                cnt += 1
                if y + 1 >= 9:
                    func(x + 1, 0)
                else:
                    func(x, y + 1)
                board[x][y] = 0
                cnt -= 1
    else:
        if y + 1 >= 9:
            func(x + 1, 0)
        else:
            func(x, y + 1)


func(0, 0)
