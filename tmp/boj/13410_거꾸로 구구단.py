N, K = map(int, input().split())

print(max(map(lambda x: int(str(x)[::-1]), [N * i for i in range(1, K + 1)])))
