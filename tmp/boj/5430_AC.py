# https://www.acmicpc.net/problem/5430

from collections import deque

input = __import__('sys').stdin.readline

for _ in range(int(input())):
    op = list(input().rstrip())
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    if arr[0] == '':
        arr.pop()
    order = 1
    ans = ''

    for o in op:
        if o == 'R':
            order = -order
        elif o == 'D':
            if len(arr) == 0:
                ans = 'error'
                break
            if order == 1:
                arr.popleft()
            else:
                arr.pop()

    if order == -1:
        arr.reverse()

    if ans == 'error':
        print(ans)
    else:
        print('[' + ','.join(arr) + ']')
