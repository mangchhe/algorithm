from sys import stdin

N, M = map(int, stdin.readline().split())

W = []
B = []

for i in range(4):

    W.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    W.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    B.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    B.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])

NList = []

def solve(board):

    WCount = 0
    BCount = 0

    for i in range(8):

        for j in range(8):

            if W[i][j] != board[i][j]:

                WCount += 1

            if B[i][j] != board[i][j]:

                BCount += 1

    return WCount if WCount < BCount else BCount

for i in range(N):

    NList.append(list(stdin.readline().strip()))

result = 56

for i in range(1, N - 6):

    for j in range(1, M - 6):

        tmpList = []

        for k in range((i - 1), 7 + i):

            tmpList.append(NList[k][(j - 1) : 7 + j])

        tmp = solve(tmpList)

        if result > tmp:

            result = tmp

print(result)