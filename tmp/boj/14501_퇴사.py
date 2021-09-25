# https://www.acmicpc.net/problem/14501

input = __import__('sys').stdin.readline

def traverse(n, total):
    global ans
    if n > N:
        return
    else:
        ans = max(ans, total)
        for i in range(n, N):
            traverse(works[i][0] + i, total + works[i][1])

N = int(input())
works = [tuple(map(int, input().split())) for i in range(N)]
ans = 0

traverse(0, 0)

print(ans)
