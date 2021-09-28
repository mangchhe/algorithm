# https://www.acmicpc.net/problem/1107

# 5459

input = __import__('sys').stdin.readline

def traverse(s):
    global ans
    if len(s) > nLen:
        return
    else:
        for number in numbers:
            now = s + str(number)
            ans = min(ans, len(now) + abs(N - int(now)))
            traverse(now)

N = int(input())
nLen = len(str(N))
M = int(input())
numbers = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(map(int, input().split())))
ans = abs(100 - N)

traverse('')

print(ans)
