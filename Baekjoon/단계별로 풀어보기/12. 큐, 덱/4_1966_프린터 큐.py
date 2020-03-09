from collections import deque
from sys import stdin

for i in range(int(input())):

    M, N = map(int, stdin.readline().split())

    M = deque(map(int, stdin.readline().split()))

    count = 0

    tmp = deque(False for i in range(len(M)))
    tmp[N] = True

    while any(tmp):

        if M[0] >= max(M):
            count += 1
            del M[0]
            del tmp[0]
        else:
            M.append(M.popleft())
            tmp.append(tmp.popleft())

    print(count)


