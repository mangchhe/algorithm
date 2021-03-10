import sys
import math

# sys.stdin = open('input.txt', 'rt')

def dfs(v):
    if len(resArr) == n:
        tmp = 0
        for i in range(n):
            tmp += exp[i] * resArr[i]
        if tmp == m:
            print(' '.join(map(str, resArr)))
            exit(0)
    else:
        for i in range(1, n + 1):
            if i not in resArr:
                resArr.append(i)
                dfs(i)
                resArr.pop()


if __name__ == '__main__':

    n, m = map(int, input().split())
    resArr = []
    exp = [1]
    for i in range(n - 1):
        exp.append(exp[i] * (n - 1 - i) // (1 + i))

    dfs(0)  