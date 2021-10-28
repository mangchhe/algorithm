# https://www.acmicpc.net/problem/16943

def dfs(n, num):
    global ans
    if num and num[0] == '0':
        return
    elif n == len(AList) and int(num) < int(B):
        ans = max(ans, int(num))
    else:
        for i in range(len(AList)):
            if not visited[i]:
                visited[i] = True
                dfs(n + 1, num + AList[i])
                visited[i] = False

A, B = input().split()
visited = [False for _ in range(len(A))]
ans = -1

AList = list(A)

dfs(0, '')

print(ans)
