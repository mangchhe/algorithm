from sys import stdin
from collections import deque

N = 0
box = []
result = deque()

def divide(y1, x1, y2, x2):

    initVal = box[x1][y1]
    doubleFor = False

    for i in range(x1, x2):
        for j in range(y1, y2):
            if initVal == 0 and box[i][j] == 1:
                initVal = 2
                doubleFor = True
                break
            elif initVal == 1 and box[i][j] == 0:
                initVal = 2
                doubleFor = True
                break
        if doubleFor:
            break

    if initVal == 0:
        print(x1,y1)
        result.append(0)
    elif initVal == 1:
        print(x1,y1)
        result.append(1)
    elif initVal == 2:
        divide(x1, y1, (x1 + x2) // 2, (y1 + y2) // 2)
        divide((x1 + x2) // 2, y1, x2, (y1 + y2) // 2)
        divide(x1, (y1 + y2) // 2, (x1 + x2) // 2, y2)
        divide((x1 + x2) // 2, (y1 + y2) // 2, x2, y2)
        result.append(')')
        result.appendleft('(')


if __name__ == '__main__':

    N = int(input())

    for _ in range(N):

        box.append(list(map(int, list(stdin.readline().strip()))))

    divide(0, 0, N, N)

    print(result)
