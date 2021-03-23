import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

def dfs(v):

    global res

    if v == n:
        print(''.join(resArr))
        res += 1
    elif v > n - 1:
        return
    else:
        for i in range(v, v + 2):
            if 0 < int(''.join(data[v:i + 1])) < 27:
                resArr.append(chr(int(''.join(data[v:i + 1])) + 64))
                dfs(i + 1)
                resArr.pop()
            else:
                break


if __name__ == '__main__':

    data = list(input())
    n = len(data)
    res = 0
    resArr = []

    dfs(0)

    print(res)