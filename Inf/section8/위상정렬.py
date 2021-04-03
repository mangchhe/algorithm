import sys
from collections import deque

sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n, m = map(int, input().split())
    data = [[0] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)
    queue = deque()

    for i in range(n):
        a, b = map(int, input().split())
        data[a][b] = 1
        degree[b] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if data[x][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
