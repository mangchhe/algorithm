import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum):

    global cnt, res

    if cnt >= res:
        return 

    if v >= n:
        return
    elif sum > m:
        return
    elif sum == m:
        if cnt < res:
            res = cnt
    else:
        for i in range(n - 1, -1, -1):
            cnt += 1
            dfs(i, sum + data[i])
            cnt -= 1


if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = float('inf')

    data.sort()

    dfs(n - 1, 0)

    print(res)

