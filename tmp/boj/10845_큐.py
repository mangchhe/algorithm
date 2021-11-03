import sys

input = sys.stdin.readline
print = sys.stdout.write

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, n):
        node = Node(n)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        res = -1
        if self.length == 1:
            res = self.head.val
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.length > 1:
            res = self.head.val
            self.head = self.head.next
            self.length -= 1
        return res
    
    def size(self):
        return self.length

    def isEmpty(self):
        return 0 if self.length > 0 else 1

    def front(self):
        return self.head.val if self.length > 0 else -1

    def back(self):
        return self.tail.val if self.length > 0 else -1

if __name__ == '__main__':

    q = Queue()
    ans = ''

    for _ in range(int(input())):
        op = input().split()
        cmd = op[0]
        if cmd == 'push':
            q.push(op[1])
        elif cmd == 'pop':
            ans += str(q.pop()) + '\n'
        elif cmd == 'size':
            ans += str(q.size()) + '\n'
        elif cmd == 'empty':
            ans += str(q.isEmpty()) + '\n'
        elif cmd == 'front':
            ans += str(q.front()) + '\n'
        elif cmd == 'back':
            ans += str(q.back()) + '\n'

    print(ans)
