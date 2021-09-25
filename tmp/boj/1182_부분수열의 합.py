# https://www.acmicpc.net/problem/1182

input = __import__('sys').stdin.readline

def traverse(n, total):
    global ans
    if n > N:
        return
    else:
        if total == S: ans += 1
        for i in range(n, N):
            traverse(i + 1, total + data[i])

N, S = map(int, input().split())
data = list(map(int, input().split()))
ans = -1 if S == 0 else 0

traverse(0, 0)

print(ans)
