from sys import stdin

N = int(stdin.readline())

for i in range(1, N + 1):

    print('*' * i)

for i in range(N - 1, -1, -1):

    print('*' * i)