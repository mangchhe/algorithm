import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v):

    global res

    if v == n:
        tmp = max(resArr) - min(resArr)
        if tmp < res and len(set(resArr)) == 3:
            res = tmp
    else:
        for i in range(3):
            resArr[i] += data[v]
            dfs(v + 1)
            resArr[i] -= data[v]

if __name__ == '__main__':
    
    n = int(input())

    data = []

    for _ in range(n):
        data.append(int(input()))

    resArr = [0 for _ in range(3)]
    res = float('INF')

    dfs(0)

    print(res)