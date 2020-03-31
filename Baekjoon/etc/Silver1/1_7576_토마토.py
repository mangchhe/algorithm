import copy
from sys import stdin



''' 시간초과 - BFS로 교체해야됨

X, Y = map(int, input().split())

tomatoBoard = []
result = 0

for i in range(Y):
    tomatoBoard.append(list(map(int,stdin.readline().strip().split())))

tmp = copy.deepcopy(tomatoBoard)

while True:
    is_cycle = 0
    for i in range(Y):
        for j in range(X):
            if tomatoBoard[i][j] == 1:
                if i + 1 < Y and tomatoBoard[i + 1][j] == 0:
                    tmp[i + 1][j] = 1
                    is_cycle += 1
                if i - 1 > -1 and tomatoBoard[i - 1][j] == 0:
                    tmp[i - 1][j] = 1
                    is_cycle += 1
                if j + 1 < X and tomatoBoard[i][j + 1] == 0:
                    tmp[i][j + 1] = 1
                    is_cycle += 1
                if  j - 1 > -1 and tomatoBoard[i][j - 1] == 0:
                    tmp[i][j - 1] = 1
                    is_cycle += 1

    tomatoBoard = copy.deepcopy(tmp)

    if is_cycle == 0:
        for i in range(Y):
            if all(tomatoBoard[i]):
                if i == Y - 1:
                    print(result)
            else:
                print(-1)
                break
        break
    else:
        result += 1

'''