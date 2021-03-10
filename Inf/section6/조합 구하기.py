import sys

# sys.stdin = open('input.txt', 'rt')

# def dfs(v):
#     if len(resArr) == m + 1:
#         print(' '.join(map(str, resArr)))
#     else:
#         for i in range(v + 1, n + 1):
#             resArr.append(v)
#             dfs(i)
#             resArr.pop()

def dfs(v):
    global cnt
    if len(resArr) == m:
        cnt += 1
        print(' '.join(map(str, resArr)))
    else:
        for i in range(v + 1, n + 1):
            resArr.append(i)
            dfs(i)
            resArr.pop()

if __name__ == '__main__':

    n, m = map(int, input().split())
    resArr = []
    cnt = 0
    dfs(0)
    print(cnt)