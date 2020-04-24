N = int(input())

box = [[' ' for j in range(N * 2)] for i in range(N)]

def solve(n, x, y):

    if n == 3:

        box[x][y] = '*'
        box[x + 1][y - 1] = '*'
        box[x + 1][y + 1] = '*'
        box[x + 2][y - 2] = '*'
        box[x + 2][y - 1] = '*'
        box[x + 2][y] = '*'
        box[x + 2][y + 1] = '*'
        box[x + 2][y + 2] = '*'

    else:

        solve(n//2, x, y)
        solve(n//2, x + n//2, y - n//2)
        solve(n//2, x + n//2, y - n//2 + n)

solve(N, 0 , N - 1)

for i in box:

    for j in i:

        print(j, end='')

    print('')