input = __import__("sys").stdin.readline

N, M = map(int, input().split())

names = {}
seq = {}

for i in range(1, N + 1):
    name = input().rstrip()
    names[name] = i
    seq[i] = name

for _ in range(M):
    n = input().rstrip()
    if n.isdigit():
        print(seq[int(n)])
    else:
        print(names[n])
