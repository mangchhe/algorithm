from collections import deque

input = __import__('sys').stdin.readline

N = int(input())

q = deque([])

for _ in range(N):
    arg = input().split()
    if arg[0] == 'push_front':
        q.appendleft(arg[1])
    elif arg[0] == 'push_back':
        q.append(arg[1])
    elif arg[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif arg[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif arg[0] == 'size':
        print(len(q))
    elif arg[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif arg[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arg[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
