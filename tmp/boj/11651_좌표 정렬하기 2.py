# https://www.acmicpc.net/problem/11651

input = __import__('sys').stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

for i in sorted(points, key = lambda x: (x[1], x[0])):
    print(' '.join(map(str, i)))
