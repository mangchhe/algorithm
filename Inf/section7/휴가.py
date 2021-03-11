import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum):

    global res

    if v > n:
        return
    else:
        res = sum if sum > res else res
        for i in range(v, n):
            dfs(i + data[i][0], sum + data[i][1])
    
if __name__ == '__main__':
    
    n = int(input())

    data = []
    res = 0
    test = []

    for _ in range(n):
        data.append(list(map(int, input().split())))

    dfs(0, 0)

    print(res)