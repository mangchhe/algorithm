# 피사노 주기
# https://sexycoder.tistory.com/62
# https://www.acmicpc.net/problem/9471

def solve(n):

    count = 0
    a = 1
    b = 1

    while True:
        count += 1
        tmp = a
        a = b
        b = (tmp + b) % n
        if a % n == 1 and b % n == 1:
            break

    return count

for i in range(int(input())):

    N, M = map(int, input().split())

    print(i+1, solve(M))