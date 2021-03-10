import sys
# sys.stdin = open('input.txt', 'rt')

def dfs(v):
    global cnt
    if len(resArr) == k:
        if sum(resArr) % m == 0:
            cnt += 1
    else:
        for i in range(v + 1, n):
            resArr.append(data[i])
            dfs(i)
            resArr.pop()

if __name__ == '__main__':
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    m = int(input())
    resArr = []
    cnt = 0

    dfs(-1)

    print(cnt)