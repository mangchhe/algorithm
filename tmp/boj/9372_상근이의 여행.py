input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M): input()
    print(N - 1)
