import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum, tsum):

    global res

    if v == n:
        return
    elif sum + (total - tsum) < res:
        return
    else:
        tmp = sum + data[v]
        if tmp < c and tmp > res:
            res = tmp
        dfs(v + 1, sum + data[v], sum + data[v])
        dfs(v + 1, sum, sum + data[v])


if __name__ == '__main__':

    c, n = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(int(input()))
    res = 0
    total = sum(data)
    dfs(0, 0, 0)

    print(res)