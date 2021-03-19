import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

def bfs(v):

    global res

    queue = deque([v])

    while True:
        tmp = []
        for q in queue:
            if q < 1 or q > 10000:
                pass
            elif q == e:
                return
            elif not visited[q]:
                visited[q] = 1
                tmp.append(q + 1)
                tmp.append(q - 1)
                tmp.append(q + 5)
        queue.extend(tmp)
        res += 1

if __name__ == '__main__':
    
    s, e = map(int, input().split())

    res = 0
    visited = [0] * 10001

    bfs(s)

    print(res)