# https://www.acmicpc.net/problem/1080

import sys

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]
ans = 0

def getAnswer(arr, arr2):
    res = True
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr2[i][j]:
                res = False
        if not res:
            break
    return res

def changeMatrix(arr, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr[i][j] = '0' if arr[i][j] == '1' else '1'

if __name__ == '__main__':
        
    if getAnswer(A, B):
        print(ans)
        sys.exit()

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                changeMatrix(A, i, j)
                ans += 1
            if getAnswer(A, B):
                print(ans)
                sys.exit()
    else:
        print(-1)
