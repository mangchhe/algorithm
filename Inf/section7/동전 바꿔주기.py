import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum):

    global cnt

    if sum == t:
        cnt += 1
    elif sum > t:
        return
    elif v > k - 1:
        return
    else:
        for i in range(cdata[v] + 1):
            dfs(v + 1, sum + ddata[v] * i)

if __name__ == '__main__':
    
    t = int(input())
    k = int(input())
    ddata = []
    cdata = []
    for i in range(k):
        a, b = map(int, input().split())
        ddata.append(a)
        cdata.append(b)
    cnt = 0

    dfs(0, 0)

    print(cnt)
