import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v):

    global cnt

    if len(resArr) == m:
        cnt += 1
        print(' '.join(map(str, resArr)))
    else:
        for i in range(1, n + 1):
            if i not in resArr:
                resArr.append(i)
                dfs(i)
                resArr.pop()

if __name__ == '__main__':

    n, m = map(int, input().split())
    resArr = []
    cnt = 0

    dfs(1)
    
    print(cnt)