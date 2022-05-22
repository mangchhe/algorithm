def traverse(x, y, num, cnt):
    if cnt == 6:
        ans.add(num)
        return

    for cx, cy in move(x, y):
        if cx < 0 or cx > 4 or cy < 0 or cy > 4:
            continue
        traverse(cx, cy, num + board[cx][cy], cnt + 1)

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

board = [input().split() for _ in range(5)]
ans = set()

for i in range(5):
    for j in range(5):
        traverse(i, j, board[i][j], 1)

print(len(ans))
