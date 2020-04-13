from sys import stdin, setrecursionlimit

setrecursionlimit(10000000)

N = 0
whiteCount = 0
blueCount = 0

paper = []

def divide(x1, y1, x2, y2):

    global whiteCount
    global blueCount

    check = paper[x1][y1]

    doubleBreak = False

    for i in range(x1, x2):
        for j in range(y1, y2):
            if check == 0 and paper[i][j] == 1:
                check = 2
                doubleBreak = True
            elif check == 1 and paper[i][j] == 0:
                check = 2
                doubleBreak = True
        if doubleBreak:
            break

    if check == 0:
        whiteCount += 1
    elif check == 1:
        blueCount += 1
    else:
        divide(x1, y1, (x1 + x2) // 2, (y1 + y2) // 2)
        divide((x1 + x2) // 2, y1, x2, (y1 + y2) // 2)
        divide(x1, (y1 + y2) // 2, (x1 + x2) // 2, y2)
        divide((x1 + x2) // 2, (y1 + y2) // 2, x2, y2)

if __name__ == '__main__':

    N = int(input())

    for _ in range(N):
        paper.append(list(map(int, stdin.readline().strip().split())))

    divide(0,0,N,N)

    print(whiteCount)
    print(blueCount)