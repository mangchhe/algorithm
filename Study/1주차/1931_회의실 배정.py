import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: (x[1], x[0]))
    res = 0
    maxVal = 0

    for d in data:
        if d[0] >= maxVal:
            maxVal = d[1]
            res += 1

    print(res)