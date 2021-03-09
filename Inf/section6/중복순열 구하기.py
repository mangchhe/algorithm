import sys

# sys.stdin = open('input.txt', 'rt')

resArr = []
cnt = 0

def dfs(v):

    global cnt

    if v == n + 1:
        return
    if len(resArr) == m:
        cnt += 1
        print(' '.join(map(str, resArr)))
    else:
        for i in range(1, n + 1):
            resArr.append(i)
            dfs(i)
            resArr.pop()

if __name__ == '__main__':

    n, m = map(int, input().split())

    dfs(1)
    print(cnt)