import sys

sys.stdin = open('input.txt', 'rt')

    
if __name__ == '__main__':
    
    n, m = map(int, input().split())

    res = [[0 for i in range(n + 1)] for i in range(n + 1)]

    for _ in range(m):
        x, y, z = map(int, input().split())
        res[x][y] = z

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(res[i][j], end=' ')
        print()