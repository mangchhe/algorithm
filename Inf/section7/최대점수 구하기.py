import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum, tsum):

    global res

    if tsum > m:
        return
    else:
        res = sum if sum > res else res
        for i in range(v + 1, n):
            dfs(i, sum + data[i][0], tsum + data[i][1])
    
if __name__ == '__main__':
    
    n, m = map(int, input().split())
    res = 0
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    dfs(-1, 0, 0)

    print(res)

