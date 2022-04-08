import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    points = []
    for _ in range(n + 2):
        points.append(list(map(int, input().split())))

    possible = [[float('INF')] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            dis = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
            if dis <= 1000:
                possible[i][j] = 1

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if possible[i][j] > possible[i][k] + possible[k][j]:
                    possible[i][j] = 1


    print('happy' if possible[0][n + 1] != float('INF') else 'sad')
