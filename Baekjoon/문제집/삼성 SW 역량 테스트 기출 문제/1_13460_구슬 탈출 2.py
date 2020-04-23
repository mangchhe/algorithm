zido = []

R_X = 0
R_Y = 0
B_X = 0
B_Y = 0

x = [0, 1, 0, -1]
y = [-1, 0, 1, 0]

N, M = map(int, input().split())

def solve():

    global R_X
    global R_Y
    global B_X
    global B_Y

    tmp = 0
    chk = 0
    result = 1

    while True:

        print(R_X, R_Y)

        if R_Y - 1 > -1 and (zido[R_X][R_Y - 1] == '.' or zido[R_X][R_Y - 1] == 'O') and zido[R_X][R_Y - 1] != 'B':
            R_Y -= 1
            chk = 0
        elif R_X + 1 < M and (zido[R_X + 1][R_Y] == '.' or zido[R_X + 1][R_Y] == 'O') and zido[R_X + 1][R_Y] != 'B':
            R_X += 1
            chk = 1
        elif R_Y + 1 < N and (zido[R_X][R_Y + 1] == '.' or zido[R_X][R_Y + 1] == 'O') and zido[R_X][R_Y + 1] != 'B':
            R_Y += 1
            chk = 2
        elif R_X - 1 > -1 and (zido[R_X - 1][R_Y] == '.' or zido[R_X - 1][R_Y] == 'O') and zido[R_X - 1][R_Y] != 'B':
            R_X -= 1
            chk = 3

        if zido[R_X][R_Y] == 'O':
            print(result)
            break

        if tmp == 0:
            tmp = chk
        elif tmp == chk:
            pass
        elif tmp != chk:
            while True:
                if (B_X + x[tmp] > -1 and B_X + x[tmp] < M) and (B_Y + y[tmp] > -1 and B_Y + y[tmp] < N) and zido[B_X + x[tmp]][B_Y + y[tmp]] == '.' and zido[B_X + x[tmp]][B_Y + y[tmp]] != 'R':
                    B_X += x[tmp]
                    B_Y += y[tmp]
                    if zido[B_X + x[tmp]][B_Y + y[tmp]] == 'O':
                        print(-1)
                        break
                else:
                    break
            tmp = 0
            result += 1


for i in range(N):

    zido.append(list(input()))

for i, val in enumerate(zido):

    try:
        R_Y = val.index('R')
        R_X = i
    except:
        pass
    try:
        B_Y = val.index('B')
        B_X = i
    except:
        pass

solve()