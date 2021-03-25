import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n, k = map(int, input().split())
    data = [int(input()) for _ in range(n)]
    data.reverse()
    res = 0

    for d in data:
        res += k // d
        k %= d

    print(res)