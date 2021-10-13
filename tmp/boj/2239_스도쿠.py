# https://www.acmicpc.net/problem/2239

# 방법 1

board = [list(map(int, input().rstrip())) for _ in range(9)]
blanks = []

def rowCheck(x, data):
    for i in range(9):
        if board[x][i] == data:
            return False
    return True

def colCheck(y, data):
    for i in range(9):
        if board[i][y] == data:
            return False
    return True

def squareCheck(x, y, data):
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == data:
                return False
    return True

def traverse(n):
    if n == len(blanks):
        for i in range(9):
            print(''.join(map(str, board[i])))
        exit()

    x, y = blanks[n]
    for i in range(1, 10):
        if board[x][y] == 0 and rowCheck(x, i) and colCheck(y, i) and squareCheck(x, y, i):
            board[x][y] = i
            traverse(n + 1)
            board[x][y] = 0

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

traverse(0)

# 방법 2
# 캐싱

def rowCheck(x, data):
    if row_cache[x][data]:
        return False
    return True

def colCheck(y, data):
    if col_cache[y][data]:
        return False
    return True

def squareCheck(x, y, data):
    if square_cache[x // 3][y // 3][data]:
        return False
    return True

def traverse(n):
    if n == len(blanks):
        for i in range(9):
            print(''.join(map(str, board[i])))
        exit()

    x, y = blanks[n]
    for i in range(1, 10):
        if board[x][y] == 0 and rowCheck(x, i) and colCheck(y, i) and squareCheck(x, y, i):
            board[x][y] = i
            row_cache[x][i] = 1
            col_cache[y][i] = 1
            square_cache[x // 3][y // 3][i] = 1
            traverse(n + 1)
            board[x][y] = 0
            row_cache[x][i] = 0
            col_cache[y][i] = 0
            square_cache[x // 3][y // 3][i] = 0

board = [list(map(int, input().rstrip())) for _ in range(9)]
blanks = []
row_cache = [[0] * 10 for _ in range(9)]
col_cache = [[0] * 10 for _ in range(9)]
square_cache = [[[0] * 10 for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        row_cache[i][board[i][j]] = 1
        col_cache[j][board[i][j]] = 1
        square_cache[i // 3][j // 3][board[i][j]] = 1
        if board[i][j] == 0:
            blanks.append((i, j))

traverse(0)
