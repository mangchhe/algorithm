import sys

sys.stdin = open('input.txt', 'rt')

def dfs(v, sum):

    global cnt
    if v > n - 1:
        return 
    elif sum == t:
        cnt += 1
    else:
        dfs(v + 1, sum + data[v])
        dfs(v + 1, sum)


if __name__ == '__main__':
    
    t = int(input())
    k = int(input())
    data = []
    n = 0
    for i in range(k):
        a, b = map(int, input().split())
        n += b
        for i in range(b):
            data.append(a)

    cnt = 0

    dfs(0, 0)

    print(cnt)
