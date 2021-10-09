# https://www.acmicpc.net/problem/11650

input = __import__('sys').stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

for i in sorted(points, key=lambda x: (x[0], x[1])):
    print(' '.join(map(str, i)))
