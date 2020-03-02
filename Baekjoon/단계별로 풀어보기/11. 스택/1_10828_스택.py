'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys

class Stack():

    def __init__(self):
        self.stackList = []

    def push(self, val):
        self.stackList.append(val)

    def pop(self):
        if len(self.stackList) == 0:
            return -1
        else:
            return self.stackList.pop(-1)

    def size(self):
        return len(self.stackList)

    def empty(self):
        if len(self.stackList) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.stackList) == 0:
            return -1
        else:
            return self.stackList[-1]


if __name__ == '__main__':

    stack = Stack()

    for i in range(int(input())):
        msg = sys.stdin.readline().strip().split()
        if msg[0] == 'push':
            stack.push(msg[1])
        elif msg[0] == 'pop':
            print(stack.pop())
        elif msg[0] == 'size':
            print(stack.size())
        elif msg[0] == 'empty':
            print(stack.empty())
        elif msg[0] == 'top':
            print(stack.top())
