'''
작성일 : 07/28
'''
from sys import stdin

count = 0


def solve(M, N):
    global count

    if M == findN:

        pass

    elif M + N < findN:

        count += 1

        solve(M + N, N // 2)

    elif M + N > findN:

        solve(M, N // 2)


findN = int(stdin.readline())

solve(0, 64)

print(count + 1)