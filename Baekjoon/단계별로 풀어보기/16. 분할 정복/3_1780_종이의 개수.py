from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

paper = []

minus = 0
zero = 0
one = 0
N = 0

def same(x1, y1, x2, y2):

    initVal = paper[x1][y1]
    doubleFor = False

    for i in range(x1, x2):
        for j in range(y1, y2):
            if initVal != paper[i][j]:
                initVal = 2
                doubleFor = True
                break
        if doubleFor:
            break
    return initVal


def divide(x1, y1, x2, y2):

    global minus
    global zero
    global one

    initVal = same(x1, y1, x2, y2)

    if initVal == -1:
        minus += 1
    elif initVal == 0:
        zero += 1
    elif initVal == 1:
        one += 1
    elif initVal == 2:
        xVal = (x2 - x1) // 3
        yVal = (y2 - y1) // 3
        for i in range(3):
            for j in range(3):
                divide(x1 + xVal * i, y1 + yVal * j, x1 + xVal * (i+1), y1 + yVal * (j+1))

if __name__ == '__main__':

    N = int(input())

    for _ in range(N):
        paper.append(list(map(int, stdin.readline().split())))

    divide(0, 0, N, N)

    print(minus)
    print(zero)
    print(one)