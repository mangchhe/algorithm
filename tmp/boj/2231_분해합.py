# https://www.acmicpc.net/problem/2231

input = __import__('sys').stdin.readline

if __name__ == '__main__':

    N = int(input())
    ans = 0

    for i in range(N, 0, -1):
        res = i
        n = i
        while n > 0:
            res += n % 10
            n //= 10
        if res == N:
            ans = i

    print(ans)
