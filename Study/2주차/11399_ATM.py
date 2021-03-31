import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))
    res = 0
    tmp = 0

    for d in sorted(data):
        tmp += d
        res += tmp

    print(res)