'''
※ 입력
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

※ 출력
1
2
2
0
1
2
-1
0
1
-1
0
3
'''

from collections import deque
from sys import stdin

# deque 모듈을 이용한 큐 구현

que = deque()

for i in range(int(input())):

    cl = stdin.readline().split()

    if cl[0] == 'push':
        que.appendleft(cl[1])
    elif cl[0] == 'pop':
        if len(que):
            print(que.pop())
        else:
            print('-1')
    elif cl[0] == 'size':
        print(len(que))
    elif cl[0] == 'empty':
        if len(que):
            print('0')
        else:
            print('1')

    elif cl[0] == 'front':
        if len(que):
            print(que[-1])
        else:
            print('-1')
    elif cl[0] == 'back':
        if len(que):
            print(que[0])
        else:
            print('-1')

# 리스트를 이용한 큐 구현(클래스) - 시간초과

class Queue():

    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.insert(0, val)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue):
            return 0
        else:
            return 1

    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]

if __name__ == '__main__':

    queue = Queue()

    for i in range(int(input())):

        cl = stdin.readline().split()

        if cl[0] == 'push':
            queue.push(cl[1])
        elif cl[0] == 'pop':
            print(queue.pop())
        elif cl[0] == 'size':
            print(queue.size())
        elif cl[0] == 'empty':
            print(queue.empty())
        elif cl[0] == 'front':
            print(queue.front())
        elif cl[0] == 'back':
            print(queue.back())