from collections import deque
from sys import stdin

N = deque()

for i in range(int(input())):

    cls = stdin.readline().split()

    if cls[0] == 'push_front':
        N.appendleft(cls[1])

    elif cls[0] == 'push_back':
        N.append(cls[1])

    elif cls[0] == 'pop_front':
        if len(N):
            print(N.popleft())
        else:
            print('-1')

    elif cls[0] == 'pop_back':
        if len(N):
            print(N.pop())
        else:
            print('-1')

    elif cls[0] == 'size':
        print(len(N))

    elif cls[0] == 'empty':
        if len(N):
            print('0')
        else:
            print('1')

    elif cls[0] == 'front':
        if len(N):
            print(N[0])
        else:
            print('-1')

    elif cls[0] == 'back':
        if len(N):
            print(N[-1])
        else:
            print('-1')